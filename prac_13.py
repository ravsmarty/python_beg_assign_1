"""
Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10

DIGITS 3

Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1


"""

#SOLUTIONS

# 1.

import math

C = 50
H = 30
D = [int(x) for x in input("Enter values for D separated by a comma: ").split(',')]

result = []
for d in D:
    Q = int(math.sqrt((2 * C * d) / H))
    result.append(Q)

print(*result)


# 2.

X, Y = [int(x) for x in input("Enter values for X and Y separated by a comma: ").split(',')]

result = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    result.append(row)

print(result)


# 3.

words = [word for word in input("Enter words separated by a comma: ").split(',')]

words.sort()

print(*words)


# 4.

words = [word for word in input("Enter words separated by a whitespace: ").split()]

words = sorted(list(set(words)))

print(*words)


# 5.

sentence = input("Enter a sentence: ")

letters = 0
digits = 0
for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)


# 6.

import re

passwords = [password for password in input("Enter passwords separated by a comma: ").split(',')]

valid_passwords = []
for password in passwords:
    if len(password) >= 6 and len(password) <= 12:
        if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]", password) and re.search("[$#@]", password):
            valid_passwords.append(password)

print(*valid_passwords)


