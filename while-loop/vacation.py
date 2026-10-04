needed_money = float(input())
current_money = float(input())
days = 0
spent_days = 0

while current_money < needed_money:
    action = input()
    if action == "spend":
        amount = float(input())
        if amount > current_money:
            amount = current_money
        current_money -= amount
        spent_days += 1
        days += 1
        if spent_days == 5:
            print("You can't save the money.")
            print(days)
            break
    elif action == "save":
        amount = float(input())
        current_money += amount
        spent_days = 0
        days += 1

    if current_money >= needed_money:
        print(f"You saved the money for {days} days.")
        break