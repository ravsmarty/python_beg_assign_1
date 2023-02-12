"""
Question 1
Create a function that takes a list of non-negative integers and strings and return a new list
without the strings.
Examples
filter_list([1, 2, &quot;a&quot;, &quot;b&quot;]) ➞ [1, 2]
filter_list([1, &quot;a&quot;, &quot;b&quot;, 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, &quot;aasf&quot;, &quot;1&quot;, &quot;123&quot;, 123]) ➞ [1, 2, 123]

Question 2
The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
opposite case.
Examples
reverse(&quot;Hello World&quot;) ➞ &quot;DLROw OLLEh&quot;
reverse(&quot;ReVeRsE&quot;) ➞ &quot;eSrEvEr&quot;
reverse(&quot;Radar&quot;) ➞ &quot;RADAr&quot;

Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create
variables first, middle and last from the given list using destructuring assignment
(check the Resources tab for some examples), where:
first ➞ 1
middle ➞ [2, 3, 4, 5]
last ➞ 6

Your task is to unpack the list writeyourcodehere into three variables, being first,
middle, and last, with middle being everything in between the first and last element. Then
print all three variables.

Question 4
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1

Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end([&quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;b&quot;], &quot;a&quot;) ➞ [&quot;b&quot;, &quot;a&quot;, &quot;a&quot;, &quot;a&quot;]


"""

# SOLUTIONS

# 1.

def filter_list(lst):
    return [x for x in lst if type(x) == int]

print(filter_list([1, 2, "a", "b"])) # [1, 2]
print(filter_list([1, "a", "b", 0, 15])) # [1, 0, 15]
print(filter_list([1, 2, "aasf", "1", "123", 123])) # [1, 2, 123]


# 2.

def reverse(txt):
    return txt[::-1].swapcase()

print(reverse("Hello World")) # DLROw OLLEh
print(reverse("ReVeRsE")) # eSrEvEr
print(reverse("Radar")) # RADAr


# 3.

lst = [1, 2, 3, 4, 5, 6]
first, *middle, last = lst
print(first) # 1
print(middle) # [2, 3, 4, 5]
print(last) # 6


# 4.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5)) # 120
print(factorial(3)) # 6
print(factorial(1)) # 1
print(factorial(0)) # 1


# 5.

def move_to_end(lst, x):
    return [y for y in lst if y != x] + [y for y in lst if y == x]

print(move_to_end([1, 3, 2, 4, 4, 1], 1)) # [3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9)) # [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a")) # ["b", "a", "a", "a"]




