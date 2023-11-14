n, k = map(int, input().split())  # Читаем количество абитуриентов и программ
limits = list(map(int, input().split()))  # Читаем контрольные цифры приёма
applicants = {}  # Словарь для хранения абитуриентов по программам

for i in range(1, k+1):
    applicants[i] = []  # Инициализируем пустой список для каждой программы

for _ in range(n):
    r, s, *priorities = map(int, input().split())  # Читаем приоритеты для абитуриента
    for program in priorities:
        if len(applicants[program]) < limits[program-1]:  # Проверяем, есть ли место на программе
            applicants[program].append(r)  # Добавляем абитуриента в список принятых
            break
    else:
        applicants[-1].append(r)  # Абитуриент никуда не поступил

for program, accepted in applicants.items():
    for a in accepted:
        print(program, end=' ')
print()
