# User is prompt to enter the following details: name, age, house number and street number.
# Once information is entered, it will result in variables for each string.

name = input("What is your name: ")
age = input("What is your age: ")
house_number = input("What is your house number: ")
street_name = input("What is your street name: ")

# Sentence is constructed with the relevant user data that has been inputted.
# Print function will generate the constructed sentence.

print(f"This is {name}. He is {age} and lives at house number {house_number} on {street_name}.")