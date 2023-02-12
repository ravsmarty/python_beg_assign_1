"""
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and
7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70

Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma
separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10

Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n&gt;1
Please write a program using list comprehension to print the Fibonacci Sequence in comma
separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13

Question 4:
Assuming that we have some email addresses in the &quot;username@companyname.com&quot; format,
please write program to print the user name of a given email address. Both user names and
company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john

Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area
of the shape where Shape&#39;s area is 0 by default.

"""

#SOLUTIONS

# 1.

def divisible_by_5_and_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter a number: "))
result = list(divisible_by_5_and_7(n))
print(','.join(map(str, result)))


# 2.

def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
result = list(even_numbers(n))
print(','.join(map(str, result)))


# 3.

def fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter a number: "))
result = list(fibonacci_sequence(n))
print(','.join(map(str, result)))


# 4.

email = input("Enter an email address: ")
username = email.split('@')[0]
print(username)


# 5.

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

s = Square(5)
print("Area of the square:", s.area())

