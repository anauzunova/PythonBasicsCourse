jury_size = int(input())
presentation_count = 0
all_presentations_average = 0

while True:
    presentation = input()

    if presentation == "Finish":
        break

    grade_sum = 0

    for _ in range(jury_size):
        grade_sum += float(input())

    average_grade = grade_sum / jury_size
    print(f"{presentation} - {average_grade:.2f}.")

    all_presentations_average += average_grade
    presentation_count += 1

final_average = all_presentations_average / presentation_count
print(f"Student's final assessment is {final_average:.2f}.")