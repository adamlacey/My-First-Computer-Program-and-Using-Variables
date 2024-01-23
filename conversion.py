 # Input all relevant data below so user can see what each variable is.
 
 # num1 has a decimal point which means it's an integer.
 # Printing the integer will generate the number as a whole. This will make 99.23 change to 99.

num1 = 99.23
new_num1 = int(num1)
print(int(new_num1))

# num2 does not have a decimal point, this means it's a float.
# Using the float command add a decimal point and changes 23 to 23.0.

num2 = 23
new_num2 = float(num2)
print(float(new_num2))

# num3 is a string and strings can contain numbers.
# When printed, it reamins the same as the varialble so the outcome is still 150.

num3 = 150
new_num3 = str(num3)
print(str(new_num3))

# num4 is a string but with quotation marks.
# Printhing this function will change it to an integer and remove the quotation marks.
# This will result the string as being 100.

string1 = "100"
new_string1 = int(string1)
print(int(new_string1))