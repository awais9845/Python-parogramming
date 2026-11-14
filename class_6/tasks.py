# easy tasks 

# Task_01
# Take the student's name, age, and marks as input and display them.


# name = input("Enter Your name: ")
# age = int(input("Enter your age: "))
# marks = int(input("Enter your marks: "))

# print("------")
# print(name)
# print("------")
# print(age)
# print("------")
# print(marks)

# task_02 
# Take a number from the user and check whether it is even or odd.


# num = int(input("Enter a number to check wether it is odd or even: "))

# if num % 2 == 0:
#     print("number is even: ", num)
# else:
#     print("number is odd", num)


# task_03 
# Take two numbers and an operator (+, -, *, /) and display the result.

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 * num2)
# print(num1 ** num2)
# print(num1 % num2)



# medium tasks 

# task_01
# Take marks of a student and display their grade using if, elif, and else.

# marks = int(input("Enter your marks to check your grade: "))

# if marks >=90:
#     print("You have got grade A.")
# elif marks >= 80:
#     print("You have got grade B.")
# elif marks >= 70:
#     print("You have got grade C.")
# else:
#     print("You have failed the test and you have been fined 100 rupees.")


# task_02 
# Keep asking the user for a password until the correct password is entered. Use a while loop.


# digit = 123

# while True:
#     password = int(input("Enter the correct password: "))
#     if password == digit:
#         print("Loged In successful!")
#         break
#     print("---------")
#     print("try again.")


# task_03
# Create a list of students and use a loop to check attendance. Use continue for absent students.


# students = ["waqar","bilal", "abubakar", "hafeez","eisa"]

# absent_student = input("Enter absent student: ")
# for i in students:
#     if i == absent_student:
#         continue
#     print(i)

# hard level practice 


# task_01

# Generate a secret number and let the user guess it. Give hints using conditional statements and loops.


# secret = 43

# while True:
#     number = int(input("Gues the number: between 40 and 50. "))
#     if number == secret:
#         print("You have entered right number")
#         break
#     print("Try again! ")

# print("Game Over")



# task_02
# Use nested loops to display multiplication tables from 1 to 5. Use break or continue where appropriate.

# for i in range(1, 10):
#     if i == 6:
#         break
#     for j in range(1, 11):
#         print(i, "x" , j , "=", i * j)

# task_03 

# Create a program that takes multiple students' names and marks, calculates their grades, and displays the final results using loops and conditional statements.



total_students = int(input("Enter the number of students: "))

for i in range(1, total_students + 1):
    print("\nStudent", i)
    print("--------")

    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    if marks >= 90:
        Grade = "A+"
    elif marks >= 80:
        Grade = "A"
    elif marks >= 70:
        Grade = "B"
    elif marks >= 60:
        Grade = "C"
    elif marks >= 50:
        Grade = "D"
    else:
        Grade = "Failed"
        
    print("----------")
    print("Student name: ", name)
    print("Student marks", marks)
    print("Stdent Grade", Grade)

print("All students names, marks and Grades are printed ")