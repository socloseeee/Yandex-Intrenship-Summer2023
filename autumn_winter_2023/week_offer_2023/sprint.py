def check(a: list[int], length, sum_) -> int:
    left = 0
    right = length - 1
    while left < right:
        if a[left] + a[right] != sum_:
            return -1
        left += 1
        right -= 1
    return sum_


N = int(input())  # задания
a = list(map(int, input().split()))  # сложности заданий
length = len(a)
# Эксперементальным путём выяснилось что попарное разбиение
# сумма для каждой пары высчитывается таким образом
sum_ = int(sum(a) / length * 2)

print(check(a, length, sum_))
