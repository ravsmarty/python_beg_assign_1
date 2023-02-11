"""
1. Write a Python program to print &quot;Hello Python&quot;?
2. Write a Python program to do arithmetical operations addition and division.?
3. Write a Python program to find the area of a triangle?
4. Write a Python program to swap two variables?
5. Write a Python program to generate a random number?

"""
                        #solutions

# 1.To print "Hello Python", you can use the following code:
print("Hello Python")

# 2.To perform arithmetical operations such as addition and division, you can use the following code:

# addition
a = 5
b = 3
c = a + b
print("The result of addition is: ", c)

# division
a = 15
b = 3
c = a / b
print("The result of division is: ", c)

# 3.To find the area of a triangle, you can use the following code:
# Calculate the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (1/2) * base * height
print("The area of the triangle is: ", area)

# 4.

a = 5
b = 3

# swapping values using a temporary variable
temp = a
a = b
b = temp
print("The value of a after swapping: ", a)
print("The value of b after swapping: ", b)

# swapping values without using a temporary variable
a, b = b, a
print("The value of a after swapping: ", a)
print("The value of b after swapping: ", b)

#5.

import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print("Random number: ", random_number)





