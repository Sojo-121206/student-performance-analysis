import csv
import matplotlib.pyplot as plt

total = 0
count = 0
topper_name = ""
topper_marks = 0

dept_total = {}
dept_count = {}

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        dept = row[1]
        marks = int(row[2])

        total += marks
        count += 1

        if marks > topper_marks:
            topper_marks = marks
            topper_name = name

        if dept in dept_total:
            dept_total[dept] += marks
            dept_count[dept] += 1
        else:
            dept_total[dept] = marks
            dept_count[dept] = 1

print("Average Marks:", total // count)
print("Topper:", topper_name, "-", topper_marks)

print("Department-wise Average:")
for d in dept_total:
    print(d, ":", dept_total[d] // dept_count[d])

# 📊 Graph
depts = list(dept_total.keys())
averages = []

for d in depts:
    averages.append(dept_total[d] // dept_count[d])

plt.bar(depts, averages)
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Department-wise Average Marks")
plt.show()
import csv
import matplotlib.pyplot as plt

total = 0
count = 0
topper_name = ""
topper_marks = 0

dept_total = {}
dept_count = {}

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        dept = row[1]
        marks = int(row[2])

        total += marks
        count += 1

        if marks > topper_marks:
            topper_marks = marks
            topper_name = name

        if dept in dept_total:
            dept_total[dept] += marks
            dept_count[dept] += 1
        else:
            dept_total[dept] = marks
            dept_count[dept] = 1

print("Average Marks:", total // count)
print("Topper:", topper_name, "-", topper_marks)

print("Department-wise Average:")
for d in dept_total:
    print(d, ":", dept_total[d] // dept_count[d])

# 📊 Graph
depts = list(dept_total.keys())
averages = []

for d in depts:
    averages.append(dept_total[d] // dept_count[d])

plt.bar(depts, averages)
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Department-wise Average Marks")
plt.show()
