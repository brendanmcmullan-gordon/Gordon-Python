userNum = int(input("Please enter a positive number:"))
num = 0
odds = 0

if(userNum%2 == 0):
    for num in range(2, userNum+1, 2):
        print(num)
elif(userNum%2 == 1):
    for num in range(1, userNum+1, 2):
        print(num)
        odds += num
    print("These odd integers add up to", odds)
