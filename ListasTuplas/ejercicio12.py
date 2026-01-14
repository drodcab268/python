matriz1 = ((1, 2, 3), (4, 5, 6))
matriz2 = ((-1, 0), (0, 1), (1,1))
result = [[0,0], [0,0]]

for x in range(len(matriz1)):
    for y in range(len(matriz2[0])):
        for j in range(len(matriz2)):
            result[x][y] += matriz1[x][j] * matriz2[j][y]

for x in range(len(result)):
    result[x] = tuple(result[x])
result = tuple(result)

for x in range(len(result)):
    print(result[x])