import csv
data_path="..\data\students.csv"
def save_students(student):
    with open(data_path, "w", newline="") as csvfile:
       field_name=["ID","Name","Age","Grade"]
       writer=csv.DictWriter(csvfile, fieldnames=field_name)
       writer.writeheader()
       writer.writerow(student)
def load_students():
    students=[]
    try:
        with open(data_path,"r",newline="") as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("فایل پیدا نشد ،")
    return students

