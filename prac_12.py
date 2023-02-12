"""
1. Write a Python program to Extract Unique values dictionary values?
2. Write a Python program to find the sum of all items in a dictionary?
3. Write a Python program to Merging two Dictionaries?
4. Write a Python program to convert key-values list to flat dictionary?
5. Write a Python program to insertion at the beginning in OrderedDict?
6. Write a Python program to check order of character in string using OrderedDict()?
7. Write a Python program to sort Python Dictionaries by Key or Value?
"""

#SOLUTIONS

# 1.

def extract_unique_values(dictionary):
    return set(dictionary.values())

my_dict = {'a':1, 'b':2, 'c':3, 'd':2}
print(extract_unique_values(my_dict))


# 2.

def sum_of_dict_items(dictionary):
    return sum(dictionary.values())

my_dict = {'a':1, 'b':2, 'c':3, 'd':2}
print(sum_of_dict_items(my_dict))


# 3.

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
print(merge_dicts(dict1, dict2))


# 4.

def convert_to_dict(list_of_tuples):
    return {key: value for key, value in list_of_tuples}

list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
print(convert_to_dict(list_of_tuples))

# 5.

from collections import OrderedDict

# create an ordered dictionary
od = OrderedDict()

# insert key-value pairs
od['first'] = 1
od['second'] = 2
od['third'] = 3

# insert key-value pair at the beginning
od.move_to_end('first', last=False)

# display the ordered dictionary
print(od)



# 6.

from collections import OrderedDict

def check_order_of_characters(string):
    char_count = OrderedDict()
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

string = 'abracadabra'
print(check_order_of_characters(string))


# 7.

def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))

def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

my_dict = {'a':1, 'b':3, 'c':2, 'd':4}
print(sort_dict_by_key(my_dict))
print(sort_dict_by_value(my_dict))
