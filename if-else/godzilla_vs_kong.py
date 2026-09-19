film_budget=float(input())
extras=int(input())
extras_clothes_price=float(input())
decor=0.1*film_budget

if extras>150:
    extras_clothes_price*=0.9
expenses=extras*extras_clothes_price+decor
leftovers=film_budget-expenses
if leftovers>=0:
    print('Action!')
    print(f'Wingard starts filming with {(leftovers):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(leftovers):.2f} leva more.')