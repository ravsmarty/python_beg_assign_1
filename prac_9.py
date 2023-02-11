"""
1. Write a Python program to check if the given number is a Disarium Number?
2. Write a Python program to print all disarium numbers between 1 to 100?
3. Write a Python program to check if the given number is Happy Number?
4. Write a Python program to print all happy numbers between 1 and 100?
5. Write a Python program to determine whether the given number is a Harshad Number?
6. Write a Python program to print all pronic numbers between 1 and 100?
"""

#programm

# 1.
def is_disarium(num):
    n = num
    sum = 0
    len_num = len(str(num))
    while n > 0:
        digit = n % 10
        sum = sum + digit ** len_num
        len_num -= 1
        n = n // 10
    return sum == num

# Test the function
print(is_disarium(135)) # True
print(is_disarium(89)) # True
print(is_disarium(8)) # False


# 2.
def is_disarium(num):
    n = num
    sum = 0
    len_num = len(str(num))
    while n > 0:
        digit = n % 10
        sum = sum + digit ** len_num
        len_num -= 1
        n = n // 10
    return sum == num

# Print all Disarium numbers between 1 and 100
for i in range(1, 101):
    if is_disarium(i):
        print(i)

# 3.
def is_happy(num):
    seen = set()
    while num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

# Test the function
print(is_happy(19)) # True
print(is_happy(7)) # True
print(is_happy(9)) # False


# 4.
def is_happy(num):
    seen = set()
    while num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

# Print all Happy numbers between 1 and 100
for i in range(1, 101):
    if is_happy(i):
        print(i)


# 5.
def is_harshad(num):
    return num % sum(int(digit) for digit in str(num)) == 0

# Test the function
print(is_harshad(18)) # True
print(is_harshad(19)) # False
print(is_harshad(10)) # True


# 6.
def is_pronic(number):
    for i in range(1, number):
        if i * (i + 1) == number:
            return True
    return False

for i in range(1, 101):
    if is_pronic(i):
        print(i)
