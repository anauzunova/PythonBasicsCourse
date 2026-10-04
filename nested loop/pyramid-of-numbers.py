n = int(input())
current = 1
row_length = 1

while current <= n:
    row = []

    for _ in range(row_length):
        if current > n:
            break
        row.append(str(current))
        current += 1

    print(" ".join(row))
    row_length += 1