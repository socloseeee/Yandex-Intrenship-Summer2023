from collections import defaultdict

n = int(input())
prefix_counters = defaultdict(int)
total_similarity = 0

for i in range(n):
    k_i = int(input())
    a_i = list(map(int, input().split()))

    prefix = 0
    for num in a_i:
        prefix = (prefix << 32) | num
        prefix_counters[prefix] += 1

for count in prefix_counters.values():
    total_similarity += (count * (count - 1)) // 2  # Близость пары массивов

print(total_similarity)
