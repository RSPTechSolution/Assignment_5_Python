students = {"Ashish": 54, "Neeraj": 68, "Karan": 87, "Raman": 75, "Ratan": 78}

student_name = input("Enter the student's name: ")

if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print("Student not found")