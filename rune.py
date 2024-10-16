def transposition(string):
    matrix = [[''] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if ((10 * i) + j) >= len(string):
                matrix[i][j] = '*'
            else:
                matrix[i][j] = string[((10*i)+j)]
    encrypted = ''
    key = [3, 1, 4, 5, 9, 2, 6, 8, 7, 0]
    for col in range(10):
        for row in range(10):
            encrypted += matrix[row][key[col]]
    return encrypted