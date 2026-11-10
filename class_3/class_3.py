# comparison operator
# used to compare two values

# result will always boolean True, False


# a = int(input("Enter a number a: "))
# b = int(input("Enter a number b: "))

# # == for equalc

# print("a is equal to b ", a == b)
# # != for not equal
# print("a is not equal to b",a != b)

# # > for greater than 
# print("a is greater than b",a > b)

# # < for less than 
# print ("a is less than b", a < b)
# # >= for greater than or equal
# print ("a is greater than or equal to b", a >= b)
# # <= for less than or equal 
# print("a is less than or equal to b" ,a <= b)



# logical operator 
# are used to combine two or more conditions


# and 
# or 
# not
#
# and 


age = int(input("Enter your age: "))

hasId = False

# and
# if both condition are true then the output will be true 
print("For And")

print(age >= 18 and hasId)

print(" hasId",hasId)

# not 
# if one condition is true the output will be true 
print("For or")
print(age >= 18 or hasId)

# not 
# it reverse the condition !True mean False and !False mean True

print("for not")

print(age >= 18 and not hasId)
a = not 10
print(type(a))
print(a)