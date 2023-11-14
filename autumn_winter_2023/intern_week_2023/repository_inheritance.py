"""Вывести номер репозитория в который нужно внести изменение Васе"""

n = int(input())
tree = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    parent = int(input())
    tree[parent].append(i)


def dfs(v):
    max_depth = 0
    max_vertex = v
    for u in tree[v]:
        depth, vertex = dfs(u)
        if depth > max_depth:
            max_depth = depth
            max_vertex = vertex
    return max_depth + 1, max_vertex

print(dfs(0)[1])
