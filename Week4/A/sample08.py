# Conditional statement
# Using if , elif (short for else if), else
# Take note of the indenting.
# Take note of the output where there are two if conditions that are both met.

age = 0

age = int(input("Enter your age:"))
if(age)>80:
    print("You are elderly")
if(age)>60:
    print("You are a senior citizen")
elif(age)>40:
    print("You are middle-aged")
elif (age > 21):
    print("You are a young adult")
elif(age>11):
    print("You are a teenager")
else:
    print("You are a child")
