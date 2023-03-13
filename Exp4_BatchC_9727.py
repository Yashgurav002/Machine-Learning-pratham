import math

def hypotenuse(a, b):
    return round(math.sqrt(a**2 + b**2), 2)
a = int(input("Enter short side 1 of triangle: "))
b = int(input("Enter short side 2 of triangle: "))

print("Hypotenuse of the triangle is: ", hypotenuse(a, b))