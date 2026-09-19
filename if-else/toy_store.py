puzzle_price=2.6
doll_price=3
bear_price=4.1
minion_price=8.2
bus_price=2
excursion_price=float(input())
puzzle=int(input())
doll=int(input())
bear=int(input())
minion=int(input())
bus=int(input())
total_toys=puzzle+doll+bear+minion+bus
total_price=puzzle_price*puzzle+doll_price*doll+bear_price*bear+minion_price*minion+bus_price*bus
if total_toys>=50:
    total_price-=1/4*total_price
else:
    total_price=puzzle_price*puzzle+doll_price*doll+bear_price*bear+minion_price*minion+bus_price*bus
income_after_tax=9/10*total_price
leftovers= income_after_tax-excursion_price

if leftovers>=0:
    print(f'Yes! {(leftovers):.2f} eu left.')
else:
    print(f'Not enough money! {abs(leftovers):.2f} eu needed.')
