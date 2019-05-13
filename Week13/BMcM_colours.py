rainbowfile = open("rainbowfile.txt", "w")

rainbowfile.write("Red")
rainbowfile.write("\nOrange")
rainbowfile.write("\nYellow")
rainbowfile.write("\nGreen")
rainbowfile.write("\nBlue")
rainbowfile.write("\nIndigo")
rainbowfile.write("\nViolet")

rainbowfile = open("rainbowfile.txt", "r")

# print(rainbowfile.readline())
# print(rainbowfile.readline())
# print(rainbowfile.readline())
# print(rainbowfile.readline())
# print(rainbowfile.readline())
# print(rainbowfile.readline())
# print(rainbowfile.readline())
# print(rainbowfile.readline())

# for i in range(7):
#     print(rainbowfile.readline())

# for i in rainbowfile:
#     print(rainbowfile.readline())

for i in rainbowfile:
    print(i)

rainbowfile = open("rainbowfile.txt", "r")

print()
print(rainbowfile.read())

rainbowfile.close()
