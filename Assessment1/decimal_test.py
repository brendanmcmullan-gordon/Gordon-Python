from decimal import *

def twoPlaces(x):
    a = Decimal(x).quantize(Decimal('.01'))
    return a

a = twoPlaces(16.6667)
print(a)
