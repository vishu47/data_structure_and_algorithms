# NOTE:
# Q1. Write a program that takes two numbers as input and checks if the first
# number is divisible by the second.

# a = int(input("enter a number : "))
# b = int(input("enter b number : "))

# if a % b == 0:
#     print(f"Yes")
# else:
#     print(f"No")

# print(f"attandance percentage {att:.2f}")

#
# classes = int(input("Number of classes held : "))
# attan = int(input("Number of classes attended : "))

# att = (classes * attan) / 100

# if att > 75:
#     print(f"allowed bcz attandance is : {att:.2f}")
# else:
#     print(f"not allowed bcz attandance is : {att:.2f}")


#  Write a program to check if number is divisible by 2 and 3 but not 8
# num = 11
# if num % 8 == 0:
#     print(f"False")
# elif num % 2 == 0 and num % 3 == 0:
#     print(f"True")
# else:
#     print(f"Not Valid")


#  Write a program to calculate bill.
# Ask the final amount from the user.
# You have to give discount and print the final bill after
# discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.

# bill = int(input("bill in rupees: "))
# if bill >= 50000:
#     dis = 30
# elif bill >= 40000 and bill <= 49999:
#     dis = 25
# elif bill >= 30000 and bill <= 39999:
#     dis = 20
# elif bill >= 10000 and bill <= 29999:
#     dis = 10
# elif bill >= 1 and bill <= 9999:
#     dis = 1
# else:
#     dis = 1

# cal = (bill * dis) / 100
# print(f"discount applied : {cal}")
# print(f"final amount : {bill -cal}")

year = int(input("enter year : "))

if year % 400 == 0:
    print(f"Leap Year")
elif year % 100 == 0:
    print(f"Not Leap Year")
elif year % 4 == 0:
    print(f"Leap Year")
else:
    print(f"Not Leap Year")
