import random

wordList = ["house", "motorcycle", "road", "apple", "telephone"]
jumble = ""

# while wordList:
#     position = random.randrange(len(wordList))
#     jumble += wordList[position] + " "
#     wordList = wordList[:position] + wordList[(position + 1):]

print(jumble)
random.shuffle(wordList)
print(wordList)

# wordList = wordList[:position] + wordList[(position + 1):]
# this expression slices the word list
# while wordList
#   while the wordList is not empty (?)
# position = random.randrange(len(wordList))
#   take a random number from the range 0,len(wordList)
# wordList = wordList[:position] + wordList[(position + 1):]
#   reassign wordList to:   the list of words from the start until "position"
#                           and from 1 after "position" until the end
# e.g. if "wordList" was ["0", "1", "2", "3"] and "position" was 2
# then the first iteration would create the list ["0", "2", "3"]







#print a word list in a random order
#random.choice(wordList) picks a random word from the list
#random.randrange(listLength) picks a random number from 0 to the specified number
#to print a list in a random order, without repeats, it must print a word from the list (using the index number), then check for

#make a list of numbers of the length of the wordlist, i.e. numList = [0, 1, 2, 3, 4, 5]
# for num in range 0, listLength
#   print(wordList[
