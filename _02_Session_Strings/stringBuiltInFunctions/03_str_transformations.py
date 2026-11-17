# Transformations
price  = "123,324"

print(price.replace(",", "."))

phone = "123-343-5445-545"
print(phone.replace("-", ""))

amount = "$1,344.99"
print(amount.replace("$", "").replace(",", ""))

#concat
first_name = "kavi"
last_name = "kumar"
print(first_name + last_name)

#format string
name = "kavi"
age = 26
city = 'banglore'

print(f"{name} is {age}, and lives in {city}.")
print(f"5 + 5 = {5+5}")
print(f"{{My name is {name}}}")

#split 
profile = "Arya-26-India" 
print(profile.split('-')) #return list of strings 

#style string
print("ha.." * 3)
print("===" * 5)

#Extraction  - (Indexes & Slicing)
 #+ve index(from start) starts from 0
 #-ve index(from end) starts from -1

name = "kavi"
print("....positive index......")
print(name[0])
print(name[0:3])
print(name[0:])
print(name[:3])
print("......negative index.....")
print(name[-4:])
print(name[-4:-2])
print(name[:-1])
print(name[0:-1])
print(name[0:0])
print(name[-1:3])
print(name[-1:-3])

date = "2026-11-15"
print(date[0:4])
print(date[:4])
print(date[-3:])