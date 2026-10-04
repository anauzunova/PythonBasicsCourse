poor_grades_limit = int(input())
total_score = 0
problems = 0
poor_grades = 0
last_problem = ""
failed = False

while poor_grades < poor_grades_limit:
    problem = input()
    if problem == "Enough":
        failed = False
        break

    grade = int(input())
    problems += 1
    total_score += grade
    last_problem = problem

    if grade <= 4:
        poor_grades += 1

    if poor_grades >= poor_grades_limit:
        failed = True
        break

if failed:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    average = total_score / problems
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {problems}")
    print(f"Last problem: {last_problem}")