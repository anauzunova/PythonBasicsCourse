budget=float(input())
videocards=int(input())
processors=int(input())
rams=int(input())
videoc_price=250
proc_price=0.35*(videoc_price*videocards)
ram_price=0.1*(videocards*videoc_price)
total=0
total=videocards*videoc_price+processors*proc_price+rams*ram_price
if videocards>processors:
    total*=85/100



if budget-total>=0:
    print(f"You have {(budget-total):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget-total):.2f} leva more!")