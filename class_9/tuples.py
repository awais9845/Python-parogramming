# tuples
# tuple is an ordered collection of items that can not be changed.
# it is immutable 

# tuple vs list 
# list is mutable 
# tuple is immutable

# syntax
# numbers = (1,2,3)
# print(numbers)
# print(type(numbers))

# also python allow to write the tuple like this
# numbers = 1,2,3,4

# print(numbers)
# print(type(numbers))

# for single value we must use comma other wise it will be considered as integer

# num = (3)
# print(type(num))

# num2 = (3,)
# print(type(num2))


# using different data types

# student_Info = ("awais khan", 9, "AI", True, 3.5)

# print(student_Info)

# tuple contstructure 
# used to change to tuple 

# numbers = [1,2,3,4]
# name = "awais khan"

# result = tuple([numbers])
# print(numbers)
# print(type(result))

# convert_tuple = tuple(name)
# print(type(convert_tuple))
# print(convert_tuple)

# numbers = tuple(range(4, 10))
# print(numbers)


# students = (
#     ("awais khan", 9),
#     ("waqas khan", 10),
#     ("waqar khan", 8)
# )

# print((students[0]))
# print((students[1]))
# print((students[2]))
# print(len(students))
# print(len(students[0]))


# numbers = (3,2,1,3,2,4,5)
# print(numbers)


# tuple packing 
# it means combining different values into a single tuple 

# student = "awais khan", 23, 9, 3.7
# print(student)
# it combines all the values in single tuple 

# name = "awais khan"
# age = 23
# grade = 9
# cgpa = 3.7

# student = name , age , grade , cgpa
# print(type(student))
# print(student)

# name = "awais khan", "waqas khan" #tuple due to separating of the comma
# name = "awais khan" # here as string
# print(type(name))

# unpacking of tuple 
# it means extracting multiple values from the tuple and storing in separate variables 

# student = ("awais khan", 23, 9, 3.7)
# name, age, grade , cgpa = student
# print(name)
# print(age)
# print(grade)
# print(cgpa)

# numbers = (1, 2, 3)
# a,b,c = numbers
# print(a)
# print(b)
# print(c)

# asterik *
# You can use * to collect multiple remaining elements into a list.

# numbers = (29, 34, 53,34, 43,23,12,43,34)
# first , *middle , before_last, last = numbers
# print(first)
# print(middle)
# print(last)
# print(before_last)

# swapping variables
# used to swap variables value in tuple 

# a =10
# b = 90
# a = b
# a , b = b , a
# print(a)
# print(b)

# tuple indexing 
# same like list 

# numbers = (1,2,3,4,5,6,6)
# positive indexing start from 0
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])

# negative indexing from opposite side from -1

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])


# touple slicing 
# slicing mean accessing a special portion
# Syntax

# # tuple[start,end,steps]
# numbers = (1,2,3,4,5,6,6)

# # print(numbers[1:6:2]) 
# print(numbers[1:3])      #by default step = 1 if not mentioned

# numbers = (10,20,30,40,50,60,70,80,90,100)

# print(numbers[::2])
# print(numbers[::3])
# numbers[::2 ] mean skip 1 element betweent the element of the selected tuple 

# to reverse the tuple 

# print(numbers[::-1]) #it reverse the tuple 

# methods of the tuple 
# tuple.count 
# used to count that how many time an element is allocated
# tuple.index
# used to find the index of the element 

# numbers = (10,20,30,40,50,60,70,40,80,90,100)

# # print(numbers.count(20))
# # print(numbers.index(40,4,10))

# print(len(numbers))
