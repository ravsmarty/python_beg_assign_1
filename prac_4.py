"""
1. Write a Python Program to Find the Factorial of a Number?
2. Write a Python Program to Display the multiplication Table?
3. Write a Python Program to Print the Fibonacci sequence?
4. Write a Python Program to Check Armstrong Number?
5. Write a Python Program to Find Armstrong Number in an Interval?
6. Write a Python Program to Find the Sum of Natural Numbers?
"""

#programms

# 1.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))

# 2.
num = int(input("Enter a number to display the multiplication table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# 3.
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nterms = int(input("How many terms? "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(1, nterms+1):
        print(fibonacci(i))

#4.
num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# 5.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num)

# 6.

num = int(input("Enter a positive integer: "))

if num < 0:
    print("Enter a positive integer")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The sum of natural numbers is", sum)

