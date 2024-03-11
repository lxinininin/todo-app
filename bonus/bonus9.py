password = input("Enter new password: ")

# {} means dictionary
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password:
    # do not confuse the upper() and isupper()
    # upper() returns String, isupper() returns Boolean
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

print(result)

# all(result.values()) means if all the values (Boolean) in result is True, it returns True, else returns False
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")