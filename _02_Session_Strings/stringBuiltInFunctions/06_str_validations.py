#Validation
country = "India"
print(country.isalpha())
country = "123ABD"
print(country.isalpha())
print(country.isalnum())
print("====" * 10)
phone = "907987907"
print(phone.isnumeric())
phone = "+91987077"
print(phone.isnumeric())