def add_student():
    students=load_students()
    new_student={
        "ID":input("Enter student ID:"),
        "Name":input("Enter student name:"),
        "age":int(input("Enter student age:")),
        "grade":input("Enter student grade:")
    }
    students.append(new_student)
    save_students(students)