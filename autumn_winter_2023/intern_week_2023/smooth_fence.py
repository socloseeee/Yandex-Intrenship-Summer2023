"""Определить наименьшую неровность забора"""
n, k = list(map(int, input().split()))  # n - кол-во досок, k - ненужные доски
length = list(map(int, input().split()))  # сами доски


while k > 0:
    avg = sum(length) / len(length)
    to_compare = [abs(number - avg) for number in length]
    del length[to_compare.index(max(to_compare))]
    k -= 1

if len(length) > 0:
    print(max(length) - min(length))
elif len(length) == 1:
    print(1)
else:
    print(0)
