n = int(input())

len_ones_sequence = 0
max_len = 0
for i in range(n):
    curr = int(input())
    if curr == 1:
        len_ones_sequence += 1
        if len_ones_sequence > max_len:
            max_len = len_ones_sequence
    else:
        len_ones_sequence = 0
print(max_len)
