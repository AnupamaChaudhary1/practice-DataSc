# math_scores = [88,76,93,65,45]
# age_list = [19,24,27,23,25]
# name_list = ["Sita",
# "Bhawana","Urgon","Sabjan","Mohit"]
# passed_list = [True,True,True,False,True]
# # Progam 1: Write a program to print the name of students and their age using the above lists.
# print("Name: Age")
# for i in range (len(name_list)):
# 	print(f"Student {str(i+1)}>>{name_list[i]}: {age_list[i]}")


# #Tuple of student details
# sita_det = ("Sita",24, 88, True)
# bhawana_det = ("Bhawana",25, 76,True)
# urgon_det = ("Urgon",27, 93,True)
# Students = [sita_det, bhawana_det, urgon_det]
# # Progam 2: Write a program to print the name of students and their age using the above sets.
# print("Name,  Age")
# for i in Students:
# 	name, age=i[0], i[1]
# 	print(f"{name},  {age}")


# # Nested dictionary
# students = {
# 	"Sita": {
# 		"math_score": 85,
# 		"age": 24,
# 		"passed": True
# 	},
# 	"Bhawana": {
# 		"math_score": 76,
# 		"age": 25,
# 		"passed": True
# 	}
# }
# # Progam 3: Write a program to print the name of students and their age.
# print("Name,  Age")
# for name in students:
#     print(f"{name}, {students[name]["age"]}")


# students = [
#     {"name": "Aarav", "math": 72, "reading": 80, "writing": 75},
#     {"name": "Sita", "math": 45, "reading": 50, "writing": 48},
#     {"name": "Bibek", "math": 90, "reading": 95, "writing": 92},
# ]
# # Program 4: Write a program to print average marks of each student. 
# for student in students:
# 	avg= (student["math"]+student["reading"]+student["writing"])/3
# 	print(f"{student["name"]}'s average marks={avg}")


# students = [
#     {"name": "Aarav", "math": 72, "reading": 80, "writing": 75},
#     {"name": "Sita", "math": 45, "reading": 50, "writing": 48},
#     {"name": "Bibek", "math": 90, "reading": 95, "writing": 92},
# ]
# # Program 5: Can you rewrite the code to calculate average as an function and use it?
# def average(student):
# 	return (student["math"]+student["reading"]+student["writing"])/3
# for student in students:
#     print(f"{student["name"]} average: {average(student)}")


# # Program 6: Create a mini dataset progamatically taking inputs in python.
# students = []
# n=int(input("How many students?"))
# for i in range (n):
#     print(f"\n Enter data for student {i+1}")
#     name=input("Name:")
#     age=int(input("Age:"))
#     student={"name":name, "age":age}
#     students.append(student)
#     print("\nStudent record:")
#     for student in students:
#         print(student)

# #Program 7: Can we store the input that we are taking into a CSV File?
# import csv
# students = []
# n=int(input("How many students?"))
# for i in range (n):
#     print(f"\n Enter data for student {i+1}")
#     name=input("Name:")
#     age=int(input("Age:"))
#     student={"Name":name, "Age":age}
#     students.append(student)
# with open("student.csv", mode="w", newline="") as file:
#     fieldnames=["Name","Age"]
#     writer=csv.DictWriter(file,fieldnames=fieldnames)
#     writer.writeheader()
#     for student in students:
#         writer.writerow(student)
# print("In csv file")

# #Program 8: Now, can we load the data from the csv file?
# import csv
# students = []
# with open("student.csv", mode="r") as file:
#         reader=csv.DictReader(file)
#         for r in reader:
#           students.append(r)
# for student in students:
#    print(student)


# Program 9: Can we import a math library to do mathematical aggregations?