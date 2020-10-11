## User Functions
import math

magnitude_max = 0.5 ** (1/2)
PI = math.pi
error = 200

def scaleAnalog(value, ref, scale):
    val = math.floor(value*scale/ref)
    return "0" + str(val+error) if val > 0 else "1" + str(abs(val-error))

def simpleControl(x, y) :
    magnitude = ((x-0.5)**2 + (y-0.5)**2)**(1/2)
    angle = math.atan2((y-0.5), (x-0.5))
    right = (angle / PI) * (magnitude/magnitude_max)
    left = ((PI - angle) / PI) * (magnitude/magnitude_max) if angle > 0 else (((-1) * PI - angle) / PI) * (magnitude/magnitude_max)
    return scaleAnalog(left, 1, 999) + "$" + scaleAnalog(left,1,999) + "$" + scaleAnalog(right, 1, 999) + "$" + scaleAnalog(right,1,999)
