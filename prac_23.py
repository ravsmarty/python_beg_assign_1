"""

Question 1
Create a function that takes a number as an argument and returns True or False depending
on whether the number is symmetrical or not. A number is symmetrical when it is the same as
its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True

Question 2
Given a string of numbers separated by a comma and space, return the product of the
numbers.
Examples
multiply_nums(&quot;2, 3&quot;) ➞ 6
multiply_nums(&quot;1, 2, 3, 4&quot;) ➞ 24
multiply_nums(&quot;54, 75, 453, 0&quot;) ➞ 0
multiply_nums(&quot;10, -2&quot;) ➞ -20

Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.

Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
 The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in
512 is (5+1+2)/3(number of digits) = 8/3=2).
 The mean will always be an integer.

"""

# SOLUTIONS

# 1.
def is_symmetrical(number):
    return str(number) == str(number)[::-1]

# 2.

def multiply_nums(nums):
    num_list = nums.split(", ")
    result = 1
    for num in num_list:
        result *= int(num)
    return result


# 3.

def square_digits(n):
    result = 0
    for digit in str(n):
        result = result * 10 + (int(digit) ** 2)
    return result


# 4.

def setify(lst):
    return sorted(list(set(lst)))


# 5.

def mean(n):
    return sum(int(digit) for digit in str(n)) // len(str(n))

