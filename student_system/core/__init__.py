from .file_handler import save_students , load_students
import os
def add_student():
    students=load_students()
    try:
        id=int(input("شماره دانش آموز:").strip())
        name=input("نام دانش آموز:").strip()
        age=int(input("سن دانش آموز:").strip())
        grade=int(input("نمره دانش آموز:").strip())

        if not id or not name or not age or not grade:
            raise ValueError("تمام فیلد ها باید پر شود")
        new_student={
            "ID":id,
            "Name":name,
            "Age":age,
            "Grade":grade
        }
        students.append(new_student)
        save_students(students)
    except ValueError:
        print("خطای ورودی")
    except Exception as e:
        print("خطا")
def remove_student():
    students=load_students()
    target_id=input("شماره دانش آموز :").strip()
    update=[s for s in students if s["ID"]!=target_id]
    if len(update) != len(students):
        save_students(update)
        print("دانش آموز حذف شد ")
    else:
        print("دانش آموز پیدا نشد ")
def view_students():
    students=load_students()
    if not students:
        print("دانش آموزی یافت نشد")
        return
    for row in students:
        print(f"{row['ID']} : {row['Name']} , {row['Age']} , {row['Grade']}")