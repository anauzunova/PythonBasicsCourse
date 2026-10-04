age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

saved_money = 0
toys_count = 0
money_taken_by_brother = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 1:
        toys_count += 1
    else:
        saved_money += birthday * 5   # 2 -> 10, 4 -> 20, 6 -> 30, ...
        money_taken_by_brother += 1

money_from_toys = toys_count * toy_price
total_money = saved_money + money_from_toys - money_taken_by_brother

if total_money >= washing_machine_price:
    left = total_money - washing_machine_price
    print(f"Yes! {left:.2f}")
else:
    needed = washing_machine_price - total_money
    print(f"No! {needed:.2f}")