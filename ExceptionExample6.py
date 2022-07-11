
userInput = int(input("Enter your age "))

try:
    if (userInput <= 0):
        raise ValueError
except ValueError as ve:
    print("User you have entered invalid input")