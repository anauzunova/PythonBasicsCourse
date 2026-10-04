change = int(round(float(input()) * 100))
coins = [200, 100, 50, 20, 10, 5, 2, 1]
coin_count = 0

for coin in coins:
    coin_count += change // coin
    change %= coin

print(coin_count)