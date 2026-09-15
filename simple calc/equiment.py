train_price=int(input())
shoes_price=0.6*train_price
jersey_price=0.8*shoes_price
ball_price=0.25*jersey_price
accessories_price=1/5*ball_price
total=train_price+shoes_price+jersey_price+ball_price+accessories_price
print(total)