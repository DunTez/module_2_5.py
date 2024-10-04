def get_matrix(n, m, value):
    if n > 0 and m > 0:
        print('Error 404')
    matrix = []
    for i in range(n):
        list = []
        matrix.append(list)
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
get_matrix(0, 2, 10)
get_matrix(6, 0, 16)
get_matrix(8, 12, 9)