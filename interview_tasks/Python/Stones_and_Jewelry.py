jewelry = input()
stones = input()

count = 0
for stone in stones:
    if stone in jewelry:
        count += 1
print(count)
