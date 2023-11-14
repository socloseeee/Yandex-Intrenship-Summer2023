k, n, m = map(int, input().split())

# создаем список раскопок
excavations = []
for i in range(n):
    d, s = map(int, input().split())
    excavations.append((d, s, i))

# сортируем раскопки по дню
excavations.sort()

# создаем список тротуаров
pavements = [-1] * m

# указатель на последнюю обработанную раскопку
last_excavation = 0

# проходим по всем дням
for day in range(1, 101):
    # двигаем указатель до следующего дня
    while last_excavation < n and excavations[last_excavation][0] == day:
        last_excavation += 1

    # проходим по всем тротуарам, где были раскопки в этот день
    for i in range(last_excavation):
        d, s, idx = excavations[i]
        if pavements[s - 1] == -1:
            pavements[s - 1] = d
        else:
            pavements[s - 1] = max(pavements[s - 1], d)

    # укладываем плитку на всех тротуарах, где ее нет
    for i in range(m):
        if pavements[i] == -1:
            print("-1")
            exit()
        elif pavements[i] < day:
            pavements[i] = day

# вычисляем количество единиц печали для каждого тротуара
sadness = 0
for i in range(m):
    sadness += day - pavements[i]

print(sadness)