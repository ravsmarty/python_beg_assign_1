"""
1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
2. Write a Python Program to Find Factorial of Number Using Recursion?
3. Write a Python Program to calculate your Body Mass Index?
4. Write a Python Program to calculate the natural logarithm of any number?
5. Write a Python Program for cube sum of first n natural numbers?
"""

#programm

# 1.
def fibonacci(n):
   if n<= 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

nterms = int(input("How many terms? "))

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibonacci(i))

# 2.
def factorial(n):
   if n == 1:
      return 1
   else:
      return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", factorial(num))

# 3.
def bmi_calculator(weight, height):
   bmi = weight / (height ** 2)
   return bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = bmi_calculator(weight, height)

print("Your BMI is", bmi)

if bmi < 18.5:
   print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
   print("You have a normal weight.")
elif bmi >= 25 and bmi < 30:
   print("You are overweight.")
else:
   print("You are obese.")

# 4.
import math

num = float(input("Enter a number: "))

ln = math.log(num)

print("The natural logarithm of", num, "is", ln)

# 5.
def cube_sum(n):
   sum = 0
   for i in range(1, n+1):
      sum += i ** 3
   return sum

n = int(input("Enter a number: "))

print("The cube sum of the first", n, "natural numbers is", cube_sum(n))
