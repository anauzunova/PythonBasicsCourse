score=int(input('Enter your score'))
bonus=0
if score<=100:
    bonus=5
elif 1000>=score>100:
    bonus=1/5*score
elif score>1000:
    bonus=0.1*score

bonus_2=0
if score%2==0:
    bonus_2=1
elif score%10==5:
    bonus_2=2

print(f'Your bonus points:{bonus+bonus_2}')
print(f'Your total score:{bonus+bonus_2+score}')