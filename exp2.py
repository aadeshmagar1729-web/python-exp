students_CET = {"Vishal", "Rohan", "Jay", "David", "Eva", "Pooja", "Dev"}
students_JEE = {"Vishal", "Jay", "Kiran", "Pooja", "Hena", "Ivy"}
students_NEET = {"David", "Eva", "Jay", "Kiran", "Neha", "Vishal"}

def union_student():
    union_students = students_CET.union(students_JEE, students_NEET)
    print("\nStudents enrolled in at least one exam (Union):")
    print(union_students)

def intersection_student():
    intersection_students = students_CET.intersection(students_JEE, students_NEET)
    print("\nStudents enrolled in all three exams (Intersection):")
    print(intersection_students)

def difference_student():
    only_CET_students = students_CET.difference(students_JEE, students_NEET)
    print("\nStudents enrolled only in CET (Difference):")
    print(only_CET_students)

while True:
    print("\n--- Student Enrolment Manager ---")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            union_student()
        elif choice == 2:
            intersection_student()
        elif choice == 3:
            difference_student()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
