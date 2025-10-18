print("=====Grade Averager=====")
grades = []
subjects = int(input("How many subjects?: "))

for i in range(1, subjects + 1):
    grade = float(input(f"Enter grade of the subject {i}: "))
    grades.append(grade)
    average = sum(grades) / subjects
    
    print("\nGrades entered:")
    for idx, grade in enumerate(grades, start=1):
        print(f"Subject {idx}: {grade}")
        print(f"\nAverage grade: {average}")


         
