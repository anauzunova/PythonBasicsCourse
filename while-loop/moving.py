width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while free_space > 0:
    command = input()

    if command == "Done":
        break

    free_space -= int(command)

if free_space >= 0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")