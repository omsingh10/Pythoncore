

char = input("Enter 'f' to convert Fahrenheit to Celsius or 'c' to convert Celsius to Fahrenheit: ")
print("You entered:", char)
if char == 'f':
    n = float(input("Enter a number: "))
    c = (n - 32) * 5 / 9
    print("Converted temperature: ", c)
elif char == 'c':
    n = float(input("Enter a number: "))
    f = (n * 9 / 5) + 32
    print("Converted temperature: ", f)
else:
    print("Invalid character entered.")