numSmall = int(input("Please enter a positive number:"))
numBig = int(input("Please enter a larger positive number:"))
num = 0
sum = 0
for num in range(numSmall, numBig+1, 1):
    print(num)
    sum += num
print(sum)
