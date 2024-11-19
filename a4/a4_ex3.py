def multiply_matrix(matrix1: list, matrix2: list) -> list:
    if len(matrix1[0]) != len(matrix2):
        return None

    result = []
    for i in range(len(matrix1)):
        result_row = []
        for j in range(len(matrix2[0])):
            result_row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
        result.append(result_row)
    return result


matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result_matrix = multiply_matrix(matrix1, matrix2)
print(result_matrix)

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10]]
result_matrix = multiply_matrix(matrix1, matrix2)
print(result_matrix)
