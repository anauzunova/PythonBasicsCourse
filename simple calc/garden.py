price_for_sqm=7.61
area=float(input())
discount=18/100*area*price_for_sqm
total=area*price_for_sqm-discount
print(f'The final price is: {total} lv.')
print(f'The discount is: {discount} lv.')