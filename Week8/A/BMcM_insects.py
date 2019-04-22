insects = ["beetle", "bug", "mayfly", "stonefly", "dragon fly"]
num = 0
print("List start:\n", insects, sep="")
print('Adding "butterfly" and "wasp"')

insects += ["butterfly", "wasp"]

print(insects)
print('Replacing "dragon fly" with "damsel fly"')

insects[4] = "damsel fly"

print(insects)
print('Deleting "wasp"')

del insects[6]

print(insects, "\n")

#Printing lists
listLength = len(insects)

for num in range(0, listLength):
    print("Index", num, insects[num])

num = 0

for num in range(0, listLength):
    print("Index", listLength-num-1, insects[listLength-num-1])

# listLength - num - 1
# listLength = length of the insect list
# insect list is 6 items, from index 0 to 5
# len(insects) will return 6, meaning it needs -1 to be used to call an index
# 'for num' counts upwards, up until 1 before the end of range
# i.e. 'for num in range 0,6' will count 0,1,2,3,4,5
# so, to start from the end (6) and move towards the beginning (0), call 'len(insects)-1' then remove 'num' from each iteration
