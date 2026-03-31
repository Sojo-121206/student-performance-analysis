import csv
import random

names = ["Arun", "Bala", "Charan", "Divya", "Elan", "Farah"]
departments = ["CSE", "ECE", "MECH"]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Dept", "Marks"])

    for i in range(200):
        name = random.choice(names)
        dept = random.choice(departments)
        marks = random.randint(40, 100)
        writer.writerow([name, dept, marks])
