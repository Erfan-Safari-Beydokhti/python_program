import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'students.csv')

def save_students(students):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, mode='w', newline='') as csvfile:
        fieldnames = ['ID', 'Name', 'Age', 'Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def load_students():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
