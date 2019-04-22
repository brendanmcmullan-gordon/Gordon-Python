#TKinter button and label change testing
from tkinter import *
import random

#number randomiser
def randomButtom():
    randomNum = random.randint(1, 1000)
    randomNum = str(randomNum)
    labelText1.set(randomNum)

#main window
window1 = Tk()
window1.title("TKinter test window")

#variable text string for label
labelText1 = StringVar()

#variable text string for button
buttonText1 = StringVar()

#label 1
label1 = Label(window1,
               font="none 24 bold",
               bg="red",
               textvariable=labelText1
               )

label1.pack()
label1['bg'] = "green"
print(label1['font'])

#button 1
button1 = Button(window1,
                 textvariable=buttonText1,
                 width=6,
                 command=randomButtom)

button1.pack(anchor="w")
print(Button.pack_info(button1))


labelText1.set("Hello, please press the button")
buttonText1.set("BUTTON")

window1.mainloop()

