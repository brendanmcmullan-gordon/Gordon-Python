from tkinter import *

window1 = Tk()

topFrame = Frame(window1)
topFrame.pack()

bottomFrame = Frame(window1)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame,
               bg="#68a2ff",
               font="courier 24",
               text="hello",
               width=20,
               padx=5)

label2 = Label(topFrame,
               bg="#ffa83f",
               font="courier 24",
               text="there",
               width=20,
               padx=5)

button1 = Button(bottomFrame,
                 fg="#bf72e0",
                 font="courier 24",
                 text="B U T T O N",
                 relief="solid")

label1.pack(side=LEFT)
label2.pack(side=RIGHT)
button1.pack(side=BOTTOM)


window1.mainloop()
