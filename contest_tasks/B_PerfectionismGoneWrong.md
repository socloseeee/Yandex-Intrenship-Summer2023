# B Task
![img_4.png](images_description/img_4.png)

![img_5.png](images_description/img_5.png)
```python
"""
Кузя может убирать 1кг льда в 1 минуту
N - Количество скульптур
X - Идеальное кол-во льда в скульптуре
T - Осталось минут до праздника
"""

N, X, T = list(map(int, input().split()))
sculptures_weight = list(map(int, input().split()))

sculptures_to_work_with = sorted(
    list(
        map(
            lambda pair: [abs(pair[1] - X), pair[0]],
            enumerate(sculptures_weight)
        )
    ), key=lambda x: x[0]
)

ideal_sculptures = []

while T >= 0 and len(ideal_sculptures) < N:
    sculpture = sculptures_to_work_with[0][0]
    if sculpture == 0:
        ideal_sculptures.append(sculptures_to_work_with[0][1] + 1)
        del sculptures_to_work_with[0]
    else:
        T -= sculptures_to_work_with[0][0]
        sculptures_to_work_with[0][0] = 0


print(len(ideal_sculptures))
print(*ideal_sculptures)

# second_variant
N, X, T = map(int, input().split())
sculptures_weight = list(map(int, input().split()))

ideal_sculptures = []
for i, weight in enumerate(sculptures_weight):
    if abs(weight - X) <= T:
        ideal_sculptures.append((abs(weight - X), i))

ideal_sculptures.sort()

result = []
for sculpture in ideal_sculptures:
    if T >= sculpture[0]:
        T -= sculpture[0]
        result.append(sculpture[1] + 1)

print(len(result))
print(*result)

```