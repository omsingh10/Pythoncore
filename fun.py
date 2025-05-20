char = input("Enter a string: ")
result = ""
for i in char:
    if i.islower():
        result += i.upper()
    elif i.isupper():
        result += i.lower()
    else:
        result += i
print(result)