import json

student = {
    "name": "Abhishek",
    "age": 19,
    "course": "B.Tech CSE"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON File Created Successfully!")