def get_matrix(n, m, values):
    matrix = []

    for i in range(n):
        matrix.append([])
        for  j in range(m):
            matrix[i].append(values)

        return matrix

result1 = get_matrix(5, 6, 30)
result2 = get_matrix(3, 5, 60)
result3 = get_matrix(7, 2, 13)
print(result1)
print(result2)
print(result3)