def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        print('Error 404')
    else:
        for i in range(n):
            list = []
            matrix.append(list)
            for k in range(m):
                matrix[i].append(value)
    print(matrix)
    return matrix


result = get_matrix(0, 15, 1)
print(result)
