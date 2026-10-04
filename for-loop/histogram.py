n = int(input())

counts = [0, 0, 0, 0, 0]

for _ in range(n):
    num = int(input())

    if num < 200:
        counts[0] += 1
    elif num < 400:
        counts[1] += 1
    elif num < 600:
        counts[2] += 1
    elif num < 800:
        counts[3] += 1
    else:
        counts[4] += 1

for count in counts:
    percentage = count / n * 100
    print(f"{percentage:.2f}%")