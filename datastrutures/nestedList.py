matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrix2 = [
    [1, 2, 3,7],
    [4, 5, 6,8],
    [7, 8, 9,8],
]

final_matrix = [] 
# for i in range(3):
#     new_matrix = []
#     for j in range(len(matrix1[i])):
#         new_matrix.append(matrix1[i][j] + matrix2[i][j]);
#     final_matrix.append(list(new_matrix))    
# print(final_matrix)

for row1, row2 in zip(matrix1, matrix2):
    new_matrix = []
    for i, j in zip(row1, row2):
        new_matrix.append(i+j)
    final_matrix.append(list(new_matrix))
print(final_matrix)    
    


