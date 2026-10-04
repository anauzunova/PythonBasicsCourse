n = int(input())
special_numbers = []

for number in range(1111, 10000):
    is_special = True

    for digit in str(number):
        if n % int(digit) != 0:
            is_special = False
            break

    if is_special:
        special_numbers.append(str(number))

print(" ".join(special_numbers))