"""
1. Write a Python program to find sum of elements in list?
2. Write a Python program to Multiply all numbers in the list?
3. Write a Python program to find smallest number in a list?
4. Write a Python program to find largest number in a list?
5. Write a Python program to find second largest number in a list?
6. Write a Python program to find N largest elements from a list?
7. Write a Python program to print even numbers in a list?
8. Write a Python program to print odd numbers in a List?
9. Write a Python program to Remove empty List from List?
10. Write a Python program to Cloning or Copying a list?
11. Write a Python program to Count occurrences of an element in a list?

"""

#programms

# 1.


def sum_list(lst):
    return sum(lst)

lst = [1, 2, 3, 4, 5]
print("Sum of elements in the list: ", sum_list(lst))

# 2.


def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

lst = [1, 2, 3, 4, 5]
print("Product of elements in the list: ", multiply_list(lst))

# 3.


def smallest_num(lst):
    return min(lst)

lst = [1, 2, 3, 4, 5]
print("Smallest number in the list: ", smallest_num(lst))


# 4.


def largest_num(lst):
    return max(lst)

lst = [1, 2, 3, 4, 5]
print("Largest number in the list: ", largest_num(lst))


# 5.


def second_largest_num(lst):
    lst.sort()
    return lst[-2]

lst = [1, 2, 3, 4, 5]
print("Second largest number in the list: ", second_largest_num(lst))


# 6.


def n_largest_elements(lst, n):
    lst.sort(reverse=True)
    return lst[:n]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 4
print(f"{n} largest elements in the list: ", n_largest_elements(lst, n))


# 7.


def even_numbers(lst):
    return [i for i in lst if i % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list: ", even_numbers(lst))


# 8.


def odd_numbers(lst):
    return [i for i in lst if i % 2 != 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Odd numbers in the list: ", odd_numbers(lst))

# 9.
def remove_empty_lists(lst):
    return [i for i in lst if i]

lst = [[], [1, 2, 3], [], [4, 5, 6], []]
print("List after removing empty lists: ", remove_empty_lists(lst))


# 10.


#copy methods
import copy

original_list = [1, 2, 3, 4, 5]
new_list = copy.copy(original_list)

print("Original List:", original_list)
print("New List:", new_list)

# slicing methods
original_list = [1, 2, 3, 4, 5]
new_list = original_list[:]

print("Original List:", original_list)
print("New List:", new_list)

# 11.

#count methods
my_list = [1, 2, 3, 4, 1, 2, 3, 1, 1, 2]

element = 1
count = my_list.count(element)

print("The element", element, "appears", count, "times in the list.")

#using loop
my_list = [1, 2, 3, 4, 1, 2, 3, 1, 1, 2]

element = 1
count = 0
for i in my_list:
    if i == element:
        count += 1

print("The element", element, "appears", count, "times in the list.")

