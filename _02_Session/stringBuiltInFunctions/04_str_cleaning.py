#Cleaning whitespaces
left_name = " max"
print(left_name)
print(left_name.lstrip())

right_name = "max "
print(right_name)
print(right_name.rstrip())

all_space_name = "      John Doe "
print(all_space_name)
print(all_space_name.strip()) #only remove spaces & tabs from both ends.

text = "###John Doe"
print(text)
print(text.strip("#"))
print(text.strip('#'))

#Case Conversion
print('\n--------CASE CONVERSION--------')
print(text.lower())
print(text.upper())
print(text.lstrip('#').lower())
print(text.lstrip('#').upper())

#challenge eg:
text = "968-Maria, ( Data Engineer ) ;; 27y  "
text = text.strip().strip('')
name = text[4:9]
role = text[13:27].strip().lower()
age = text[-3:-1]
print(f"name: {name} | role: {role} | age: {age}")
