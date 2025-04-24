import csv
import os

DATA_PATH = './data/students.csv'

def save_students(students):
    try:
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        with open(DATA_PATH, mode='w', newline='') as csvfile:
            fieldnames = ['ID', 'Name', 'Age', 'Grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    except Exception:
        print(" خطا هنگام ذخیره اطلاعات.")

def load_students():
    if not os.path.exists(DATA_PATH):
        return []
    try:
        with open(DATA_PATH, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except Exception:
        print(" خطا هنگام بارگذاری فایل.")
        return []
