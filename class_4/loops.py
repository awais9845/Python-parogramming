# loops 
# used to execute a block of code repeatadly without writing the same code again and again.

# for 
# while 


# syntax

# for i in range(start,end,steps): by default step is 1
    # print()

# for i in range(0,100, 2):
#     print(i)
# for i in range(10,5,-1):
#     print(i)

name = "Awais khan"

print(name.index("a"))

# for char in name:
#     print(char)

# list 
# will study later 

students = ["awais", "waqas", "waqar"]

# for name in students:
#     print(name)

# while syntax 
# variable

# while condition:
#     print()
#     increment or decrement 

i = 0

# while i <= 4:
# while i % 2 == 0 and i <= 10:
#     print(i)
#     i += 2

# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1

    
i = 0
# while i < len(students):
#     print(students[i])
#     i +=1

# for each later 
while i < len(name):
    print(name[i])
    i += 1

# for indexing 
num = 0
while num < len(name):
    print("indexing", num)
    num+= 1