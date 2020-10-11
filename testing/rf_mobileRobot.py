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

def nrfConfig(isListen, address):
    nrf.listen = isListen
    if isListen:
        nrf.open_rx_pipe (rxPipeNum, address)
    else :
        nrf.open_tx_pipe(address)
    return nrf


def receiver(NRF, address):
    if NRF.any():
        value = NRF.recv()
        print(value)

n = nrfConfig(True, b'coop1')
while True:
    receiver(n, b'coop1')

