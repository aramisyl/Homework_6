def transpose(massive):
    massive_size = len(massive)
    new_massive = [[0] * massive_size in range(massive_size)]
    for i in range(massive_size):
        for j in range(massive_size):
            new_massive[i][j] = massive[j][i]
    return new_massive

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
