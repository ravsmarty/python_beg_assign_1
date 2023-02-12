"""
Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.

Question 2:
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Question 3:

Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class.

Question 4:
Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].

Question 5:
Please write a program to compress and decompress the string &quot;hello world!hello
world!hello world!hello world!&quot;.

Question 6:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.
"""

#SOLUTIONS

# 1.

class DivisibleBySeven:
  def __init__(self, n):
    self.n = n
  
  def divisible_by_seven(self):
    for i in range(self.n + 1):
      if i % 7 == 0:
        yield i

n = 100
gen = DivisibleBySeven(n)
for num in gen.divisible_by_seven():
  print(num)


# 2.

def word_frequency(text):
  words = text.split()
  frequency = {}
  for word in words:
    frequency[word] = frequency.get(word, 0) + 1
  sorted_frequency = sorted(frequency.items(), key=lambda x: x[0])
  return sorted_frequency

text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
print(word_frequency(text))


# 3.

class Person:
  def getGender(self):
    pass

class Male(Person):
  def getGender(self):
    print("Male")

class Female(Person):
  def getGender(self):
    print("Female")

person = Male()
person.getGender()

person = Female()
person.getGender()


# 4.

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:
  for verb in verbs:
    for obj in objects:
      print(f"{subject} {verb} {obj}.")


# 5.

import zlib

def compress_string(string):
  compressed = zlib.compress(string.encode('utf-8'))
  return compressed

def decompress_string(compressed_string):
  decompressed = zlib.decompress(compressed_string).decode('utf-8')
  return decompressed

string = "hello world!hello world!hello world!hello world!"
compressed = compress_string(string)
print("Compressed:", compressed)

decompressed = decompress_string(compressed)
print("Decompressed:", decompressed)


# 6.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
