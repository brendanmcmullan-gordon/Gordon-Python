from tkinter import *

def destroyFrame():
    innerFrame2.pack(padx=5,
                     pady=5)
    innerFrame1.destroy()


window1 = Tk()
window1.title("Window 1")

mainFrame = Frame(window1,
                  bg="red")
mainFrame.pack()

innerFrame1 = Frame(mainFrame)
innerFrame1.pack(padx=5,
                 pady=10)

innerFrame2 = Frame(mainFrame)

button1 = Button(innerFrame1,
                 fg="blue",
                 width=20,
                 command=destroyFrame,
                 text="B U T T O N 1")
button1.pack()

label1 = Label(innerFrame2,
               bg="green",
               padx=5,
               pady=5,
               font="courier 48 bold",
               text="YES")
label1.pack()

entry1 = Entry(innerFrame2,
               width=20,
               bg="white")
entry1.pack(padx=5,
            pady=5)

window1.mainloop()
