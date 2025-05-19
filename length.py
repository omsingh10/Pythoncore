n = float(input("Enter the length: "))
toknown = input("Enter the unit of length (m, cm, or km): ")
if toknown == "m":
    want = input("Enter the unit you want to convert to (cm or km): ")
    if want == "cm":
        print("length in cm is", n * 100)
    elif want == "km":
        print("length in km is", n / 1000)
    else:
        print("Invalid unit")
elif toknown == "cm":
    want = input("Enter the unit you want to convert to (m or km): ")
    if want == "m":
        print("length in m is", n / 100)
    elif want == "km":
        print("length in km is", n / 100000)
    else:
        print("Invalid unit")
elif toknown == "km":
    want = input("Enter the unit you want to convert to (m or cm): ")
    if want == "m":
        print("length in m is", n * 1000)
    elif want == "cm":
        print("length in cm is", n * 100000)
    else:
        print("Invalid unit")
else:
    print("Invalid unit")