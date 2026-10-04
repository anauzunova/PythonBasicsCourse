temperature=int(input())
time_of_day=input()
outfit=''
shoes=''
if 10<=temperature<=18:
    if time_of_day=='Morning':
        outfit='Sweatshirt'
        shoes='Sneakers'
    elif (time_of_day=='Afternoon') or (time_of_day=='Evening'):
        outfit='Shirt'
        shoes='Moccasins'
elif 18 < temperature <= 24:
    if time_of_day=='Afternoon':
            outfit='T-Shirt'
            shoes='Sandals'
    elif (time_of_day=='Morning') or (time_of_day=='Evening'):
            outfit='Shirt'
            shoes='Moccasins'
elif temperature >= 2:
    if time_of_day=='Morning':
            outfit='T-Shirt'
            shoes='Sandals'
    elif (time_of_day=='Afternoon'):
            outfit='Swim Suit'
            shoes='Barefoot'
    elif (time_of_day=='Evening'):
            outfit='Shirt'
            shoes='Moccasins'

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")