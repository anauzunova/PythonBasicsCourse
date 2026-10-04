flower = input()
count = int(input())
budget = int(input())

prices = {
    'Roses': 5,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3,
    'Gladiolus': 2.50
}

total_price = count * prices[flower]

if flower == 'Roses' and count > 80:
    total_price *= 0.90
elif flower == 'Dahlias' and count > 90:
    total_price *= 0.85
elif flower == 'Tulips' and count > 80:
    total_price *= 0.85
elif flower == 'Narcissus' and count < 120:
    total_price *= 1.15
elif flower == 'Gladiolus' and count < 80:
    total_price *= 1.20

if budget >= total_price:
    print(f'Hey, you have a great garden with {count} {flower} and {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')