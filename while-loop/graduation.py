student_name = input()
total_grade = 0
grades_count = 0
failed_times = 0
current_class = 1

while current_class <= 12:
    grade = float(input())
    total_grade += grade
    grades_count += 1

    if grade < 4.00:
        failed_times += 1
        if failed_times > 1:
            print(f"{student_name} has been excluded at {current_class} grade")
            break
    else:
        failed_times = 0

    if current_class == 12:
        average = total_grade / grades_count
        print(f"{student_name} graduated. Average grade: {average:.2f}")
        break

    current_class += 1