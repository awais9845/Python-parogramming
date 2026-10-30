

num_1 = int(input("Please enter first number"))
num_2 = int(input("Plese enter second number"))


sum = num_1 + num_2;
dif = num_1 - num_2;
mult = num_1 * num_2;
divi = num_1 / num_2;
modu = num_1 % num_2;

print(modu)

print(sum)
print(dif)
print(mult)
print(divi)

age = int(input("Enter your age."))

if age < 18:
    print("you are not eligible for voting")
else:
    print("You are eligible for voting")

marks = int(input("Please enter your marks to check your grad"))


if marks > 100:
    print("You have entered wrong numbers")
elif marks >= 90:
    print("You are in Grad A")
elif marks >= 80:
    print("You are in Grad B")
elif marks >= 70:
    print("You are in Grad C")
elif marks >= 60:
    print("You are in Grad D")
elif marks >= 50:
    print("You are in Grad E")
else:
    print("You are failed")