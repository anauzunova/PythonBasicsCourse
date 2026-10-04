month=input()
nights=int(input())
studio=0
apartment=0
if (month=='May') or (month=='October'):
    if nights>14:
        studio=70/100*50
        apartment=65
    elif nights>7:
        studio=95/100*50
        apartment=65
    else:
        studio=50
        apartment=65
elif (month=='June') or (month=='September'):
    studio=75.20
    apartment=68.70
elif (month=='July') or (month=='August'):
    studio=76
    apartment=77

if ((month=='June') or (month=='September')) and nights>14:
    studio-=20/100*studio

if nights>14:
    apartment-=0.1*apartment

ap_stay_price=apartment*nights
st_stay_price=a=studio*nights

print(f"Apartment: {ap_stay_price:.2f} lv.")
print(f"Studio: {st_stay_price:.2f} lv.")