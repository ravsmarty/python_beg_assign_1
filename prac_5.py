
"""
1. Write a Python Program to Find LCM?
2. Write a Python Program to Find HCF?
3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
4. Write a Python Program To Find ASCII value of a character?
5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

"""

#programm

# 1.
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The LCM of", num1,"and", num2,"is", lcm(num1, num2))

# 2.
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The HCF of", num1,"and", num2,"is", compute_hcf(num1, num2))

# 3.
dec = int(input("Enter a decimal number: "))

print("The binary representation of", dec, "is", bin(dec).replace("0b", ""))
print("The octal representation of", dec, "is", oct(dec).replace("0o", ""))
print("The hexadecimal representation of", dec, "is", hex(dec).replace("0x", ""))

# 4.
c = input("Enter a character: ")
print("The ASCII value of", c, "is", ord(c))

# 5.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice(1/2/3/4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
