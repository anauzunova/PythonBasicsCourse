
actor_name = input()
points = float(input())
n = int(input())

for _ in range(n):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2

    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    needed = 1250.5 - points
    print(f"Sorry, {actor_name} you need {needed:.1f} more!")