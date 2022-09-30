import sys

# if, else and elif
# Example 1:

bank_balance = 9000
withdraw_money = 5000

if bank_balance >= withdraw_money:
    print("success")

if bank_balance <= withdraw_money:
    print("insufficient funds")

# Example 2:

if bank_balance >= withdraw_money:
    print("success")

else:
    print("insufficient funds")

# Examplo 3:

color = str(input("choose a color:white, black or red: \n"))

if color == "white":
    print("you're right!")

elif color == "black" or color == "red":
    print("try again")

else:
    sys.exit("invalid option")

# Example 4 - Python Nested if

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# Example 5 - ternary conditional operator
a = 2
b = 3

1 if a > b else -1
# Output is -1
