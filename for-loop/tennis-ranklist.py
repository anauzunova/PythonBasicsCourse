n = int(input())
points = int(input())

wins = 0

for _ in range(n):
    stage = input()

    if stage == "W":
        points += 2000
        wins += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

average = points // n  

win_percentage = wins / n * 100

print(f"Final points: {points}")
print(f"Average points: {average}")
print(f"{win_percentage:.2f}%")