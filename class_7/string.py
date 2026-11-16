# string
# string is the collection of characters or alphabet that are enclosed in quotation marks

# example 

# name = "Awais khan"

# print(name)

# indexing 
# start from 0. 
# print(name[0])
# print(name[3])

# negative indexing is also possible 
# negative start from opposite side 
# print(name[-1])
# n
# print(name[-3])

# print(len(name))
# print(str.upper(name))
# print(str.lower(name))


# list methods

# .upper() used to write in upper case

# name = "Awais khan"

# print(name.upper())

# # .lower() used to write in lower case

# print(name.lower())

# .stripe() used to remove the space from the beggining and the end 

# name = " Awais khan "
# print(name)
# # print(name.strip())

# # .replace to replace either a letter or the word 

# print(name.replace("a","o"))
#  # first one show the letter or the word which we want to replace and the second replace that word with the second word.


# language = "i have learnt javaScript"
# print(language)
# print(language.replace("javaScript", "Python"))

# split 
# used to separate string or divide it into pieces and convert it into list 

# languages = "urdu english pashto"
# print(languages.split())

# bottles = "cook dew fanta sting booster"
# print(bottles.split())


# .join
# it is opposite to the split 
# used to combine multiple strings into one string using separator operator 

# students = ["awais", "musa", "eisa"]
# # language = "I have learnt python"
# # print(language.split())

# result = " ".join(students)
# print(result)

# date = ["02", "3", "2026"]
# print("-".join(date))

# result = "-".join(date)
# print(result)


# .find()
# used to find the index of a character or a word in a string 

# language = "I have learnt Python"

# result = language.find("Python")

# print(result)

# # python is case sensitive 

# result = language.find("Python")
# print(result)


# .count()
# used to count how many time a char or word is present

# name = "awais khan"

# print(name.count("khan"))


# language = "I have learnt python"
# print(language.count("python"))


# startswith() and endwith()
# always give tue or false value 


language = "I am learning Python"

print(language.startswith("am"))
print(language.endswith("Python"))