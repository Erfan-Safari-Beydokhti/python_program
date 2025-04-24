import csv
import os
from logging import exception

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'students.csv')

def save_students(students):
    try:
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        with open(DATA_PATH, mode='w', newline='') as csvfile:
            fieldnames = ['ID', 'Name', 'Age', 'Grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    except Exception as e:
        print("خطا هنگام ذخیره اطلاعات")
def load_students():
    if not os.path.exists(DATA_PATH):
        return []
    try:
        with open(DATA_PATH, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except Exception as e:
        print("خطا هنگام بارگزاری فایل")
        return []