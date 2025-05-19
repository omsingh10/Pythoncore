import math

def rectangle():
    a = int(input("Enter a length: "))
    b = int(input("Enter a width: "))
    para = 2 * (a + b)
    print("The perimeter of the rectangle is", para)

def triangle():
    a = int(input("Enter a base: "))
    b = int(input("Enter a height: "))
    area = 0.5 * a * b
    print("The area of the triangle is", area)

def sinterest():
    p = int(input("Enter a principal: "))
    r = int(input("Enter a rate: "))
    t = int(input("Enter a time: "))
    si = (p * r * t) / 100
    print("The simple interest is", si)

def cinterest():
    p = int(input("Enter a principal: "))
    r = int(input("Enter a rate: "))
    t = int(input("Enter a time: "))
    ci = p * (1 + r / 100) ** t
    print("The compound interest is", ci)

def circle():
    r = int(input("Enter a radius: "))
    area = math.pi * r ** 2
    print("The area of the circle is", area)

print("Choose an operation:")
print("1. Perimeter of rectangle")
print("2. Area of triangle")
print("3. Simple interest")
print("4. Compound interest")
print("5. Area of circle")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        rectangle()
    case 2:
        triangle()
    case 3:
        sinterest()
    case 4:
        cinterest()
    case 5:
        circle()
    case _:
        print("Invalid choice.")