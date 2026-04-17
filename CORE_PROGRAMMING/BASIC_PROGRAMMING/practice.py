# Task: Student Eligibility Filter using Sets
# Problem Statement

# You are given two sets:
# Students who submitted assignments
# Students who attended classes

# You need to determine:

# Who is eligible (both submitted + attended)
# Who is not eligible
# Who only did one of the activities
# Input
# submitted = {"Geeta", "Rahul", "Amit", "Sneha"}
# attended = {"Amit", "Sneha", "Kiran", "Geeta"}
# Requirements
# Find Eligible Students

# Students who are in both
# Find Not Eligible Students

# Students who are:
# Only submitted OR
# Only attended


# create data set including studentname,student id,subject,marks and fileter student marks based on taken marks if >50%,70%firstclass >85% distinction ,and also give them grade based percentage "A","B","C


dummy_data=[
  {"name": "kunal", "id": 1, "subject": "Math", "marks": 50},
  {"name": "rahul", "id": 2, "subject": "Science", "marks": 70},
  {"name": "Aman", "id": 3, "subject": "English", "marks": 90}

]



ans_data={

}

for student in dummy_data:
  if student["marks"]>=85:
    ans_data[student["name"]]="A"
  elif student["marks"]>=70:
    ans_data[student["name"]]="B"
  elif student["marks"]>=50:
    ans_data[student["name"]]="C"
  else:
    ans_data[student["name"]]="Fail"

print(ans_data)


user_input=input("Enter a String: ")

ans_str=""

for char in user_input[::-1]:
  ans_str+=char

print("Reversed String: ",ans_str)


