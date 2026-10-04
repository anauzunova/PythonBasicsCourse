width = int(input())
length = int(input())
remaining_pieces = width * length

while remaining_pieces > 0:
    command = input()

    if command == "STOP":
        break

    remaining_pieces -= int(command)

if remaining_pieces > 0:
    print(f"{remaining_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(remaining_pieces)} pieces more.")