total = 0.0

while True:
    value = input()
    if value == "NoMoreMoney":
        break

    amount = float(value)

    if amount < 0:
        print("Invalid operation!")
        break

    total += amount
    print(f"Increase: {amount:.2f}")

print(f"Total: {total:.2f}")