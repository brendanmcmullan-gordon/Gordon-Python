from tkinter import *

#Key press
def click():
    enteredText = textentry.get() #get text from text box
    output.delete(0.0, END)
    try:
        definition = testDict[enteredText]
    except:
        definition = "Sorry, that is an invalid entry"
    output.insert(END, definition)

#exit function
def closeWindow():
    window.destroy()
    exit()

#Main
window = Tk()
window.title("Window Title")
window.configure(background="black")

#Photo
photo1 = PhotoImage(file="bird.gif")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

#Label1
Label(window, text="This is some text. Enter some text:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

#Text Entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#Submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

#Label2
Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

#output
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#Dictionary
testDict = {
    'entry1': 'This is the first entry in the dictionary.', 'entry2': 'This is the second entry in the dictionary'
}

#exit label
Label(window, text="Press button to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

#exit button
Button(window, text="EXIT", width=14, command=closeWindow).grid(row=7, column=0, sticky=W)

window.mainloop()
