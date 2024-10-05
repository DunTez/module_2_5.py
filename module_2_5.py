def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        print('Error 404')
        return
    matrix = []
    for i in range(n):
        list = []
        matrix.append(list)
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


result = get_matrix(14, 14, 10)
print(result)
for i in result:
    print(*i)
