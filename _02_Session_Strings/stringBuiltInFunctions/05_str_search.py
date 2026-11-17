#Search in String
phone = "+91-63688688"
print(phone.startswith("+91"))
print(phone.endswith("21"))

# present in the string
email = "asdf@gmail.com"
print(email.endswith("gmail.com"))
print("@" in email)
print(email in "@")

#find in the string(return the first index on the word/char from the string)
print(phone[phone.find('-') + 1:])