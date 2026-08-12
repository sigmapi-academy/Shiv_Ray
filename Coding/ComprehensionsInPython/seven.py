
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result = [value for row in matrix for value in row ]
print(matrix)
print('Flattened the matrix')
print(result)