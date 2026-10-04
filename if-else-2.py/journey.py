budget = float(input())
season = input().lower()

if budget <= 100:
	destination = "Somewhere in Bulgaria"
	if season == "summer":
		accommodation = "Camp"
		spent = budget * 0.30
	else:
		accommodation = "Hotel"
		spent = budget * 0.70
elif budget <= 1000:
	destination = "Somewhere in Balkans"
	if season == "summer":
		accommodation = "Camp"
		spent = budget * 0.40
	else:
		accommodation = "Hotel"
		spent = budget * 0.80
else:
	destination = "Somewhere in Europe"
	accommodation = "Hotel"
	spent = budget * 0.90

print(destination)
print(f"{accommodation} - {spent:.2f}")
