import csv

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Abhishek", 19, "B.Tech CSE"])
    writer.writerow(["Rahul", 20, "B.Tech CSE"])

print("CSV File Created Successfully!")