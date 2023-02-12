"""
1. Write a Python program to find words which are greater than given length k?
2. Write a Python program for removing i-th character from a string?
3. Write a Python program to split and join a string?
4. Write a Python to check if a given string is binary string or not?
5. Write a Python program to find uncommon words from two Strings?
6. Write a Python to find all duplicate characters in string?
7. Write a Python Program to check if a string contains any special character?
"""

# SOLUTION

# 1.

# Here's a program to find words that are greater than a given length k:

def find_words_greater_than_k(sentence, k):
    words = sentence.split()
    result = [word for word in words if len(word) > k]
    return result

sentence = "This is a sample sentence"
k = 4
print(find_words_greater_than_k(sentence, k))

# 2.

# Here's a program to remove the i-th character from a string:
def remove_ith_char(string, i):
    return string[:i] + string[i+1:]

string = "hello"
i = 2
print(remove_ith_char(string, i))

# 3.

# Here's a program to split and join a string:
def split_and_join(string, delimiter):
    split_string = string.split(delimiter)
    joined_string = delimiter.join(split_string)
    return joined_string

string = "hello,world"
delimiter = ","
print(split_and_join(string, delimiter))


# 4.

# Here's a program to check if a given string is a binary string or not:
def is_binary_string(string):
    return all(c in "01" for c in string)

string = "10101"
print(is_binary_string(string))

# 5.

def find_uncommon_words(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    uncommon = set1.symmetric_difference(set2)
    return list(uncommon)

str1 = "this is a sample string"
str2 = "another sample string"
print(find_uncommon_words(str1, str2))

# 6.

def find_duplicate_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [char for char, count in char_count.items() if count > 1]
    return result

string = "hello world"
print(find_duplicate_chars(string))

# 7.

import re

def has_special_char(string):
    pattern = r"[!@#$%^&*(),.?\":{}|<>]"
    return bool(re.search(pattern, string))

string = "hello world!"
print(has_special_char(string))


