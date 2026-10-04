n = int(input())

max_number = float('-inf')
min_number = float('inf')

for _ in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number} Min number: {min_number}")