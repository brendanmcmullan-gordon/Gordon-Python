num1 = float(input("Please enter a number"))
num2 = float(input("Please enter a different number"))

if (num1 == num2):
    print("Please enter two different numbers")

else:
    if (num1>num2):
        print("%.2f is greater than" %num1, "%.2f" %num2)

    else:
        print("%.2f is greater than" %num2, "%.2f" %num1)
