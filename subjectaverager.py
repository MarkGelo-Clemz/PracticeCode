while True:
    print("=====Grade Averager=====")
    grades = []
    subjects = int(input("How many subjects?: "))
    
    for i in range(1, subjects + 1):
        grade = float(input(f"Enter grade of the subject {i}: "))
        grades.append(grade)
        
        
    average = sum(grades) / subjects
    print(f"\nYour average grade is: {average:.2f}")
    
    again = input("Do you wish to calculate again? (y/n): ")
    if again != 'y':
        print("Goodbye...")
    else: 
        print("Invalid input")
        break
