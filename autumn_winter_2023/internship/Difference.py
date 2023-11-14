def calculate_diversity(count_a, count_b):
    diversity = 0

    # Подсчет разнообразия на основе словарей
    for card in count_a:
        if card not in count_b:
            diversity += count_a[card]
        else:
            diversity += max(0, count_a[card] - count_b[card])

    for card in count_b:
        if card not in count_a:
            diversity += count_b[card]

    return diversity


n, m, q = map(int, input().split())
player_a = list(map(int, input().split()))
player_b = list(map(int, input().split()))

# Инициализация словарей для подсчета количества карт
count_a = {}
count_b = {}
for card in player_a:
    count_a[card] = count_a.get(card, 0) + 1
for card in player_b:
    count_b[card] = count_b.get(card, 0) + 1

results = []

for _ in range(q):
    type_change, player, card = input().split()
    card = int(card)

    if type_change == "1":
        if player == "A":
            count_a[card] = count_a.get(card, 0) + 1
        else:
            count_b[card] = count_b.get(card, 0) + 1
    else:
        if player == "A":
            count_a[card] -= 1
            if count_a[card] == 0:
                del count_a[card]
        else:
            count_b[card] -= 1
            if count_b[card] == 0:
                del count_b[card]

    diversity = calculate_diversity(count_a, count_b)
    results.append(str(diversity))

print(" ".join(results))
