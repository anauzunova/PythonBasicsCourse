n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

total_sum = sum(numbers)

for x in numbers:
    if x == total_sum - x:
        print("Yes")
        print(f"Sum = {x}")
        break
else:
    max_num = max(numbers)
    sum_without_max = total_sum - max_num
    diff = abs(max_num - sum_without_max)
    print("No")
    print(f"Diff = {diff}")