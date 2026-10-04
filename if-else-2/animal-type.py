animal = input()

if animal == 'dog':
    animal = 'mammal'
elif animal in ('crocodile', 'snake', 'tortoise'):
    animal = 'reptile'
else:
    animal = 'unknown'

print(animal)