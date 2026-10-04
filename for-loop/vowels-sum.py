text = input().lower()

values = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

total = 0

for ch in text:
    if ch in values:
        total += values[ch]

print(total)