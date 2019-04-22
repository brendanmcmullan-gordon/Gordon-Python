userWord = input("Please enter a word.")
backWord = ""
wordLength = len(userWord)
length = wordLength

for num in range (0, wordLength):
    #print(userWord[length-1])
    backWord += userWord[length-1]
    length += -1
print(backWord)

# for ch in userWord:
#     backWord += ch
# print(backWord)


#strings are just arrays/tuples
#get string length
#add the last character of the string to another var
