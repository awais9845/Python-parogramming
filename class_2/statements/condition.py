# conditional statement 

# it will look to the condition if the the condition is true then will execute the block of code. other wise will skip the code if false 
# we use in python if, elif and else


# for example 

# age = int(input("Please enter your age "))

# if age >= 18:
#     print("You are eligible for the voting")
# else:
#     print("You are not eligible for the voting")


marks = int(input("Please enter your marks "))

if marks > 100 :
    print("You have entered something extra")
elif marks >= 90:
    print("You have got grade A")
elif marks >= 80:
    print("You have got grade B")
elif marks >= 70:
    print("You have got grade C")
else:
    print("You are failed")


