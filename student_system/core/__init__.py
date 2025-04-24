from .file_handler import save_students , load_students
import os
def add_student():
    students=load_students()
    new_student={
        "ID":input("Enter student ID:"),
        "Name":input("Enter student name:"),
        "Age":int(input("Enter student age:")),
        "Grade":input("Enter student grade:")
    }
    students.append(new_student)
    save_students(students)
def remove_student():
    students=load_students()
    target_id=input("شماره دانش آموز :")
    update=[s for s in students if s["ID"]!=target_id]
    if len(update) != len(students):
        save_students(update)
        print("دانش آموز حذف شد ")
    else:
        print("دانش آموز پیدا نشد ")
def view_students():
    students=load_students()
    for row in students:
        print(f"{row['ID']} : {row['Name']} , {row['Age']} , {row['Grade']}")