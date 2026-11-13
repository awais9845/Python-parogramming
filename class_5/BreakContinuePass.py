# break continue and pass 

# these are used for different purposes

# when the condition become true and we don't want anymore to run the parogram we use the break statement

# syntax 

# if variable in sequence: 
#     if condition:
#         break



# for num in range(1, 6):
#     if num == 3:
#         break
#     print(num)


# num = 0

# while num <= 6:
#     if num == 3:
#         break
#     print(num)
#     num += 1

# digit = 123

# while True:
#     password = int(input("please enter the password"))
#     if password == digit:
#         print("you have entered correct passwrod")
#         break
#     print("Incorrect password! Try again.")


# continue
# when the condition become true we only skip that and the remaining loop is running on samely.

# Syntax

# for variable in sequence:
#     if condition:
#         continue
#     print(variable)



# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# years = [2025, 2026, 2027]

# for i in years:
#     if i == 2026:
#         continue
#     print(i)

students = ["awais","musa", "eisa", "waqar", "bilal", "waqas"]

absent_student = input("Enter the absent student name: ")


for i in students:
    if i == absent_student:
        continue
    print(i)