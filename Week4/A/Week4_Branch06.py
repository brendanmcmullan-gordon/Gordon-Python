num1 = float(input("Please enter a number"))
num2 = float(input("Please enter a different number"))
bigger = 0.0
smaller = 0.0
if (num1 == num2):
    print("Please enter two different numbers")

else:
    if (num1>num2):
        bigger = num1
        smaller = num2
        print("bigger = %.2f" %bigger, ", smaller = %.2f" %smaller)
    else:
        bigger = num2
        smaller = num1
        print("bigger = %.2f" %bigger, ", smaller = %.2f" %smaller)
