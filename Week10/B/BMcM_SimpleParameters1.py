def add(n1,n2):
    answer = n1 + n2
    return(answer)

def subtract(n1,n2):
    if n1 > n2 or n1 == n2:
        answer = n1 - n2
    elif n2 > n1:
        answer = n2 - n1
    return answer

def multiply(n1, n2):
    answer = n1 * n2
    return answer

def divide(n1,n2):
    answer = n1 / n2
    return answer

choice = None
num1 = None
num2 = None

while choice != 0:
    choice = input("""
        What function would you like to perform?
        0 - Exit
        1 - Add
        2 - Subtract
        3 - Multiply
        4 - Divide
    """)

    if choice == "1":
        num1 = int(input("Please enter the first number you wish to add: "))
        num2 = int(input("Please enter the second number you wish to add: "))
        print(num1, "plus", num2, "equals", add(num1,num2))
        input("\nPress ENTER to continue.")

    elif choice == "2":
        num1 = int(input("Please enter the first number you wish to subtract: "))
        num2 = int(input("Please enter the second number you wish to subtract: "))
        if num1 > num2 or num1 == num2:
                print(num1, "minus", num2, "equals", subtract(num1,num2))
        elif num2 > num1:
                print(num2, "minus", num1, "equals", subtract(num1,num2))
        input("\nPress ENTER to continue.")

    elif choice == "3":
        num1 = int(input("Please enter the first number you wish to multiply: "))
        num2 = int(input("Please enter the second number you wish to multiply: "))
        print(num1, "multiplied by", num2, "equals", multiply(num1,num2))
        input("\nPress ENTER to continue.")

    elif choice == "4":
        num1 = int(input("Please enter the first number you wish to divide: "))
        num2 = int(input("Please enter the second number you wish to divide: "))
        print("\n", num1, "divided by", num2, "equals", divide(num1,num2))
        input("\nPress ENTER to continue.")


# print(add(5,9))
# print(subtract(14,19))
# print(multiply(6,11))
# print(divide(15,3))
