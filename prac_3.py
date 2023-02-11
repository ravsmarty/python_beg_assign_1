"""
1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
2. Write a Python Program to Check if a Number is Odd or Even?
3. Write a Python Program to Check Leap Year?
4. Write a Python Program to Check Prime Number?
5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
"""

# 1.
def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter a number: "))
check_number(num)

# 2. 
def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
check_odd_even(num)

# 3.
def check_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if check_leap_year(year):
    print("Leap")
else:
    print("Not a leap")

# 4.
def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if check_prime(num):
    print("Prime")
else:
    print("Not Prime")

# 5.
def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

start = 1
end = 10000
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if check_prime(num):
        print(num)
