import re
password = input()
if len(password) < 8:print("Invalid password!")
elif not re.search("[a-z]", password):print("Invalid password!")
elif not re.search("[A-Z]", password):print("Invalid password!")
elif not re.search("[0-9]", password):print("Invalid password!")
elif not re.search("[$#@]", password):print("Invalid password!")
else:print("Valid password!")
