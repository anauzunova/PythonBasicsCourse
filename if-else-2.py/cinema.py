screening_type=input()
price=-1
rows=int(input())
columns=int(input())
capacity=rows*columns
if screening_type== 'Premiere':
    price=12
elif screening_type=='Normal':
    price=7.5
elif screening_type=='Discount':
    price=5

if price>=0:
    income=(f'{capacity*price:.2f} leva')
    print(income)
else:
    print('')
    