import board
import digitalio as dio
from circuitpython_nrf24l01 import RF24
import time
import busio

addressLength = 5 # available for int [3,5]
rxPipeNum = 0
transmitInterval = 0.2

ce = dio.DigitalInOut(board.D18)
csn = dio.DigitalInOut(board.D16)

# config.txt -> dtoverlay=spi1-1cs NEEDED?
board.MOSI = 20 #raspi4b+ spi1
board.SCK = 21 #raspi4b+ spi1
board.MISO = 19 #raspi4b+ spi1

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
nrf = RF24(spi, csn, ce, address_length=addressLength)

startCode = "@"

def encodeData(value, code):
    result = startCode + code+ " "
    result = result.encode("utf-8")
    for letter in str(value):
        result += letter.encode("utf-8")
    return result

def decodeData(value):
    try :
        result = value.decode("utf-8")
        print(result)
        if result[0] != "@":
            return {"code" : "!", "value" : 0 }
        else :
            data = result.split()[1]
            return {"code" : result[1], "value" : data.split("'")[0]}
    except :
        return {"code" : "#", "value" : 0 }



def nrfConfig(isListen, address):
    nrf.listen = isListen
    if isListen:
        nrf.open_rx_pipe (rxPipeNum, address)
    else :
        nrf.open_tx_pipe(address)
    return nrf

def transmitter(NRF, address, value, code):
    value = encodeData(value, code)
    print("sending : {}".format(value))
    result = NRF.send(value)
    time.sleep(transmitInterval)

def receiver(NRF, address):
    if NRF.any():
        value = decodeData(NRF.recv())
        if value['code'] != '#':
            return value
    return {"code" : "*", "value" : "none"}
