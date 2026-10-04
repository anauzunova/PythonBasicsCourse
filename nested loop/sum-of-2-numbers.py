start = int(input())
end = int(input())
magic_number = int(input())

combination_number = 0
found = False

for first in range(start, end + 1):
    for second in range(start, end + 1):
        combination_number += 1

        if first + second == magic_number:
            print(
                f"Combination N:{combination_number} "
                f"({first} + {second} = {magic_number})"
            )
            found = True
            break

    if found:
        break

if not found:
    total_combinations = (end - start + 1) ** 2
    print(
        f"{total_combinations} combinations - "
        f"neither equals {magic_number}"
    )