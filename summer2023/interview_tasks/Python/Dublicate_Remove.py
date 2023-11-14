n = int(input())
unique = [None]
for i in range(n):
    curr = int(input())
    if curr != unique[-1]:
        print(curr)
        unique.append(curr)
