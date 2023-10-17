# taking input from the user
# a = int(input("enter the number: "))
# print("user enter a number: ", a)

# if else statement

# age = int(input("enter ur age: "))
# if age>= 18:
#     print("user is adult")
# else:
#     print("user is not adult")

# score = int(input("Enter ur score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >=80:
#     print("Grade B")
# elif score >=70:
#     print("Grade C")
# else:
#     print("Grade F")

# nested if statements:- condition inside condition 
# x=10
# y=5
# if x>y:
#     print("x is greater than y")
#     if x>15:
#         print("x is also greater than 15")
#     else:
#         print("x is not greater than 15")
# else:
#     print("x is not greater than y")

# Loops in python
# fruits = ['apple','banana','cherry']
# for x in fruits:
#     print(x)

# number = [1,2,3,4,5,6,7]
# for i in number:
#     print(i)


# while loop example
# count = 0
# while count < 5:
#     print(count)
#     count+=1

# break is used to skip out of block, continue us used for skipping the current condition
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue # it will skip the current condition.....
#     print(i)

# looping through dictonires
# person = {
#     'name': "sidharth",
#     'age': 22,
#     'city': "BHOPAL"
# }
# for key,value in person.items():
#     print(f'{key}:{value}')


#loop control with else:- we can use else block with the loop which can execute when the loop complete without hittin the loop
# for i in range(5):
#     if i ==3:
#         break
#     print(i)
# else:
#     print("loop completed without a break")


# final conclusion example
user_input = int(input("enter the integer: "))
# check the number is even or odd
if user_input % 2 ==0:
    print(f"{user_input} is a even number")
else:
    print(f"{user_input} is a odd number")

# using a for loop to print number from 1 to user-input number
print("Number from 1 to ", user_input)
for i in range(1, user_input+ 1):
    print(i)

 

