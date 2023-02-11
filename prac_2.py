"""
1. Write a Python program to convert kilometers to miles?
2. Write a Python program to convert Celsius to Fahrenheit?
3. Write a Python program to display calendar?
4. Write a Python program to solve quadratic equation?
5. Write a Python program to swap two variables without temp variable?

"""
# 1.
def km_to_miles(kilometers):
    return kilometers * 0.621371

kilometers = float(input("Enter distance in kilometers: "))
print("Distance in miles:", km_to_miles(kilometers))

# 2.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

# 3.
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(calendar.month(year, month))

# 4.
import math

def solve_quadratic(a, b, c):
    if a == 0:
        return -c/b

    delta = b*b - 4*a*c
    sqrt_delta = math.sqrt(abs(delta))
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    return x1, x2

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
solutions = solve_quadratic(a, b, c)

if type(solutions) is tuple:
    print("Solutions:", solutions)
else:
    print("Solution:", solutions)


# 5.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, "b =", b)
