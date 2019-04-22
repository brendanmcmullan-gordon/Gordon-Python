startNum = 0
endNum = 0
increment = 0
startNum = int(input("Please enter the number you wish to start counting at:"))
endNum = int(input("Please enter the number you wish to finish counting at:"))
increment = int(input("Please enter the increment you wish to count in:"))

for num in range (startNum, endNum+1, increment):
    print(num)
