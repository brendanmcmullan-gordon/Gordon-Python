userWord = input("Please enter a word:")
vowels = ("a","e","i","o","u")
vowelsInWord = ""


for ch in userWord:
    if ch in vowels:
        vowelsInWord += ch + " "

print("Your word is", userWord)
print("The vowels in your word are:", vowelsInWord)

