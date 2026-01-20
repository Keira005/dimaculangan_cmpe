import math
import mathplotlib.pyplot as plt

myIntegerA = 55
myIntegerB = 28
myIntegerC = 10
myFloatA = 50.50
myFloatB = 10.20
myComplexA = 10-5j
myComplexB = 24 - 12j

mySum = myIntegerA + myIntegerB
print(mySum)
myDiff = myIntegerA - myIntegerB
print(myDiff)
myProd = myIntegerA * myIntegerB
print(myProd)

result = 2 ** 6
print(result)

myQo = myIntegerA / myIntegerB
print(myQo)
myRoundedQo = round(myQo, 2)
print(myRoundedQo)
remainder = myIntegerA % myIntegerC
print(remainder)
remainder = myIntegerA % myIntegerB
print(remainder)

myComProd = myComplexA * myComplexB
print(myComProd)
print(5*4*3*2*1)
print(math.factorial(5))
cos_90_deg = math.cos(math.radians(60))
print(cos_90_deg)