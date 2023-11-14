"""
7
0 0
0 2
2 2
0 -2
2 -2
2 -1
2 1
2
1 3
#
2
"""
from copy import deepcopy
from math import sqrt

N = int(input())  # Количество городов
city_coords = [list(map(int, input().split())) for _ in range(N)]  # Координаты каждого города
k = int(input())  # Максимальное расстоние без дозаправки
from_, to = input().split()  # Из какого города в какой

print(city_coords)

adjacency_matrix = []
for i in range(N):
    row = []
    for j in range(N):
        value = sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + (city_coords[i][1] - city_coords[j][1]) ** 2)
        if i != j and value <= k:
            row.append(round(value, 2))
        else:
            row.append(-1)
    adjacency_matrix.append(deepcopy(row))
    row.clear()
print(*adjacency_matrix, sep='\n')


def find_pathes(matrix, k, N, from_, to):
    all_pathes = [[] for _ in range(N)]
    if -1 < matrix[int(from_) - 1][int(to) - 1] <= k:
        return 1
    for i in range(N):
        for j in range(N):
            if i != j and -1 < matrix[i][j] <= k:
                all_pathes[i].append(j)
                if j == int(to) - 1:
                    print(all_pathes[i])
                    return len(all_pathes[i])
    return -1


best_path = find_pathes(adjacency_matrix, k, N, from_, to)
print(best_path)
