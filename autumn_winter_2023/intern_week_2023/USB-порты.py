n = int(input())  # Кол-во USB-портов
m = int(input())  # Кол-во USB-гаджетов
c2 = int(input())  # Цена развлетвителя с 1-го USB на 2
c5 = int(input())  # Цена развлетвителя с 1-го USB на 5

if n <= m:
    m -= n
    parts_4 = m // 4
    if parts_4 == 0:
        min_price = min(m * c2, c5)
        print(min_price)
    else:
        price = min(4 * parts_4 * c2, c5 * parts_4)
        m -= 4 * parts_4
        if m != 0:
            price += min(m * c2, c5)
        print(price)
else:
    print(0)
