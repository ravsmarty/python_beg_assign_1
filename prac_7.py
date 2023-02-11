"""
1. Write a Python Program to find sum of array?
2. Write a Python Program to find largest element in an array?
3. Write a Python Program for array rotation?
4. Write a Python Program to Split the array and add the first part to the end?
5. Write a Python Program to check if given array is Monotonic?
"""

#programm

# 1.
def sum_array(array):
    sum = 0
    for num in array:
        sum += num
    return sum

array = [1, 2, 3, 4, 5]
print("Sum of array:", sum_array(array))

# 2.
def largest_element(array):
    largest = array[0]
    for num in array:
        if num > largest:
            largest = num
    return largest

array = [1, 2, 3, 4, 5, 6, 7]
print("Largest element in array:", largest_element(array))


# 3.
def rotate_array(array, k):
    for i in range(k):
        first_element = array.pop(0)
        array.append(first_element)
    return array

array = [1, 2, 3, 4, 5]
k = 2
print("Array after rotation:", rotate_array(array, k))

# 4.
def split_and_add(array, k):
    first_part = array[:k]
    second_part = array[k:]
    second_part.extend(first_part)
    return second_part

array = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Array after splitting and adding:", split_and_add(array, k))

# 5.
def is_monotonic(array):
    increasing = True
    decreasing = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            increasing = False
        if array[i] < array[i + 1]:
            decreasing = False
    return increasing or decreasing

array = [1, 2, 2, 3, 4, 5]
print("Is array monotonic:", is_monotonic(array))
