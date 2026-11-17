#Numeric types
x = 5
y = 5.7
z = 2 + 3j
print(type(x))
print(type(y))
print(type(z))

#numeric conversion
print("---------Numeric conversions---------")
a = "123"
print(type(a))
print(a * 3)
b = int(a)
print(type(b))
print(b * 2)
print(float(b))
c = 4.2134
print(int(c))
d = "5.1234"
print(float(d))

#complex types (used in advanced mathematical situations)
e = 4 #real
f = 5 #imaginary
print(complex(e, f))