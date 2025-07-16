# Ask user for their name
# name = input("What is your name? ")

# Say hello to user
# print("Hello " + name + "\nGood morning, How are you?")


# name = input("What is your name? ")

# print("hello,", end="")
# print(name)
# print("Hello,", name, sep="") # The sep parameter puts its input in between the other arguments of the print function


# String Methods
# Ask user for name
# name = input("What is your full name? ")

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Splitting user's name into first name, middle name and last name
# first_name, middle_name, last_name = name.split(" ")

# Say hello to user
# print(f"Hello, {middle_name}.")

name = input("What is your name? ")
age = input("What is your age? ")
location = input("Where do you live? ")

# string concatenation

# print("Hello, " + name + ". you are " + age + " years old and you live in " + location + ".")
# f strings

print(f"Hello, {name}. You are {age} years old and you live in {location}.")
