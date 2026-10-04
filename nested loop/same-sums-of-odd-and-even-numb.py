start = int(input())
end = int(input())
matching_numbers = []

for number in range(start, end + 1):
    digits = str(number)
    even_position_sum = 0
    odd_position_sum = 0

    for index, digit in enumerate(digits):
        if index % 2 == 0:
            even_position_sum += int(digit)
        else:
            odd_position_sum += int(digit)

    if even_position_sum == odd_position_sum:
        matching_numbers.append(str(number))

if matching_numbers:
    print(" ".join(matching_numbers))