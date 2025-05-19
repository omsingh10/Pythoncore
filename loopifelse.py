for a in range(1,16):
    if a%3==0 and a%5==0:
        print(a ," is fizzbuzz")
    elif a%3==0:
        print(a ," is fizz")
    elif a%5==0:
        print(a ," is buzz")
    else:
        print(a)