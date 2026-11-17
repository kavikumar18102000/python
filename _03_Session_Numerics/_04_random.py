import random
#random
print(random.random()) #generates floating point random values
print(random.randint(1,6)) #generates integer random values

#challenge(check random number is even or odd)
print((random.randint(1, 100) & 1) == 0)