from tkinter import *

#Key press
def click():
    enteredText = textentry.get() #get text from text box
    output.delete(0.0, END)
    userMessage = "Hello, " + str(enteredText)
    output.insert(END, userMessage)

#exit function
def closeWindow():
    window.destroy()
    exit()

#Main
window = Tk()
window.title("Brendan - My TKinter")
window.configure(background="black")

#Photo
photo1 = PhotoImage(file="bird.gif")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

#Label1
Label(window, text="Please enter your name:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

#Text Entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#Submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

#Label2
Label(window, text="\nMessage:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

#output
output = Text(window, width=75, height=1, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#exit label
Label(window, text="Press button to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

#exit button
Button(window, text="EXIT", width=14, command=closeWindow).grid(row=7, column=0, sticky=W)

window.mainloop()
