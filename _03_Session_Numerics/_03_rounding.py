import math
#Numeric rounding

#Non-negative number
print(2-8)
print(abs(2-8)) #gives non-negative number

#rounding number
print(round(3.34))
print(round(3.565))
print(round(3.5487, 2))
print(round(-3))

#rounding to lowest whole number
print(math.floor(3.34))
print(math.floor(3.999))

#rounding to near largest whole number
print(math.ceil(3.34))
print(math.ceil(3.99))

#rounding to whole  number(no near or larger, just cuts the decimal values)
print(math.trunc(3.34))
print(math.trunc(4.99))
print(int(4.99))