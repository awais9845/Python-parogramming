# lists 
# list is a collection of multiple data stored inside in one variable.

# numbers = [12, 34,59, 34]
# print(numbers)


# nested list 

# students =[
#     ["Awais khan", "23", "3rd"],
#     ["waqas khan", "43" , "4th"],
#     ["Waqar khan", "32", "5th"]
# ]
# print(students)
# print(students[1][0])


# methods of lists

# list.append()

# used to add element at the end of the list 

# numbers = [1,2,4,5]
# numbers.append(6)
# print(numbers)

# names = ["awais khan", "waqas khan ", "waqar khan"]

# names.append("musa khan")
# print(names)

# len(list)
# used to  find the length of the list 

# names = ["awais khan", "waqas khan", "bilal"]
# # print(names[1])
# # print(len(names))
# print(names[-1]) # it will print the last one value 


# list.remove(value)
# used to remove value from the list 

# languages = ["python", "cpp", "java", "javascript"]
# print(languages)
# languages.remove("cpp")
# print(languages)

# .extend()
# used to add multiple values to the list at the end 
# machine_languages = ["python", "cpp", "java", "javascript"]
# human_languages = ["Urdu", "english", "Pashto"]

# machine_languages.extend(human_languages)

# print(machine_languages)
# print(machine_languages.extend(human_languages))


# list.insert(index, value)
# it is used to add the data in list on a specific location using indexing value which start from 0. 


# human_languages = ["Urdu", "english", "Pashto"]
# human_languages.insert(0 , "german") # 0 showing indexing
# print(human_languages)
# human_languages.remove("german")
# print(human_languages)

# .pop(indexing)
# used to remove the element using the indexing.
# numbers = [23,32,12,43]
# # removed_item = numbers.pop()  # by default -1 which is the last value
# removed_item = numbers.pop(0)  
# print(removed_item)
# print(numbers)



# list.clear()
# used remove all the data of the list and make it empty 


# numbers = [23,32,12,43]
# numbers.clear()
# names = ["Awais khan ", "waqas khan", "waqar khan"]
# numbers.extend(names)
# print(numbers)

# .index(value, start, end)
# used to find the index of the element in list 
# start and end is optional 


# numbers = [23,32,12,43,23,54,45,34,23]
# # element_index = numbers.index(23)
# # element_index = numbers.index(23,2)
# element_index = numbers.index(23,5,12)

# print(element_index)

# list.count()
# used to count that how many times an element is present

# numbers = [23,32,23,43,23]
# print(numbers.count(23))
# print(numbers.count(32))

# list.sort()
# used to arrange element in either ascending or descending orders
# for descending order reverse=True

# numbers = [32,43,23,12,32,53,34,25,64]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# list.reverse()
# used to reverse list 

# numbers = [32,43,23,12,32,53,34,25,64]
# numbers.reverse()
# print(numbers)

# list.copy()
# used to make the copy of the original list and do not affect if any change made in the top list

# numbers = [1,2,3]
# numbers_copy = numbers.copy()
# # numbers.append(4)
# numbers_copy.append(4)

# print("old list",numbers)
# print("copy of list",numbers_copy)
# print(type(numbers))
# print(type(numbers_copy))

# other useful methods 
# numbers = [1,2,3,4]
# print(max(numbers))
# print(min(numbers))
# print(len(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(any(numbers)) #True because if one element is true
# numbers = [1,2,3,0]
# print(all(numbers)) #false because zero is false value if one is false, it will give false value

# numbers = [1,2,3]
# print(all(numbers)) #true because all values are true if all value is true it will give true value.

# .enumerate()
# The enumerate() function is used to loop through an iterable and get both the index and value of each element at the same time.

# names = ["Awais", "Waqas", "Ali", "Usman"]
# result = enumerate(names)
# print(list(result))



# zip()
# The zip() function is used to combine two or more iterables together by matching their elements according to their positions.


# names = ["awais", "waqar", "waqas"]
# age = [22,19, 17]

# # result = zip(names,age)
# # print(list(result))

# for name, age in zip(names, age):
#     print(f"name {name}: age {age}")

# for index, name in enumerate(names):
#     print(index,  name)