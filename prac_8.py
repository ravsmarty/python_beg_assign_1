"""
1. Write a Python Program to Add Two Matrices?
2. Write a Python Program to Multiply Two Matrices?
3. Write a Python Program to Transpose a Matrix?
4. Write a Python Program to Sort Words in Alphabetic Order?
5. Write a Python Program to Remove Punctuation From a String?
"""

# programm

# 1.
# adding two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(add_matrices(matrix1, matrix2))

# 2.
# multiply two metrices

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        return "Error: Incompatible matrices"
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            sum = 0
            for k in range(cols1):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(multiply_matrices(matrix1, matrix2))

# transposig metrices
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        result.append(row)
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix))

# 4.
# sorting words in alphabets
def sort_words_alphabetically(words):
    words.sort()
    return words

words = ['apple', 'banana', 'cherry', 'date']
print(sort_words_alphabetically(words))


# 5.

import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans("", "", string.punctuation))

input_string = "Hello, World! How are you today?"
print(remove_punctuation(input_string))
