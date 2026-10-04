budget=int(input())
season=input()
fishermen=int(input())
rent=0
if season=='Spring':
    rent=3000
elif season=='Summer':
    rent=4200
elif season=='Autumn':
    rent=4200
elif season=='Winter':
    rent=2600

if 6>=fishermen:
    rent-=0.1*rent
elif 7<=fishermen<=11:
    rent-=15/100*rent
elif fishermen>=12:
    rent-=1/4*rent

if fishermen%2==0:
    if (season=='Spring') or (season=='Summer') or (season=='Winter'):
        rent-=1/20*rent

leftover= budget-rent
if leftover>=0:
    print(f"Yes! You have {leftover:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(leftover):.2f} leva.")