def palyndrome_time(n, m):
    count = 0
    length = max(len(str(n - 1)), len(str(m - 1)))
    if n <= m:
        for i in range(n):
            if int(str(i).zfill(length)[::-1]) < m:
                print(f"{str(i).zfill(length)}:{str(i).zfill(length)[::-1]}")
                count += 1
    else:
        for i in range(m):
            if int(str(i).zfill(length)[::-1]) < n:
                print(f"{str(i).zfill(length)[::-1]}:{str(i).zfill(length)}")
                count += 1
    return count


n, m = list(map(int, input().split()))  # n - кол-во часов, m - кол-во минут

print(palyndrome_time(n, m))
