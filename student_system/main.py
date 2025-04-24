from core import add_student , view_students , remove_student
def main ():
    while True:
        print("\n ♦♦♦ Student Management System ♦♦♦ ")
        print("1. نمایش لیست دانش آموزان ")
        print("2. افزودن دانش آموز ")
        print("3. حذف دانش آموز ")
        print("4. خروج ")
        choice=input("انتخاب شما: ").strip()
        if choice=="1":
            view_students()
        elif choice=="2":
            add_student()
        elif choice=="3":
            remove_student()
        elif choice=="4":
            print("خروج از برنامه ")
            break
        else:
            print("گزینه نامعتبر ")
if __name__ == "__main__":
    main()