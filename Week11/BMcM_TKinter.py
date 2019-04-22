#Python Glossary GUI OO code
# ref video (min:sec) - https://www.youtube.com/watch?v=_lSNIrR1nZU
# ref - documentation https://docs.python.org/3/library/tkinter.html
# ref - documentation https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref - documentation http://www.tkdocs.com/tutorial/index.html


from tkinter import *                           # (0:50 mins)

# event functions (10:30 mins)
def onClickSubmitButton():                      # submit button event handler
        userEnteredText = textbox.get()         # get the enterd text from the Entry text box
        outputTextField.delete(0.0, END)        # (14:30 mins)delete all of the output field text contents
        # (15:00) exception
        try:                                    # (15:00 mins) exception 
            definition = python_dictionary[userEnteredText] # get the definition that matches the key value of the eneterd text
        except:
            definition = " no match for key value entered"
        outputTextField.insert(END, definition)  # (15:50 mins)
        
def  onClickExitButton():                       # (18:30 mins) exit button event handler        
    window.destroy()
    exit()
    


#main window (1:30 mins)
window = Tk()
window.title("Python Glossary")
window.configure(background="white")

#photo displayed with a Label  (2:00) - display your photo add me.gif into the same folder as the .py file
photo = PhotoImage(file="bird.gif")
Label(window, image=photo, bg="white").grid(row=0,column=0,sticky=W) # using grid (3:30  mins) layout , sticky W = West // OR E = East

# display text using - Label  (05:30 mins)
Label(window, text="Enter a python operator or command to see its definition", bg="white", font="none 12 bold").grid(row=1,column=0,sticky=W) # using grid layout

# textbox for text entry - Entry (8:15 mins)
textbox = Entry(window, width=20, bg="white")
textbox.grid(row=2, column=0,sticky=W)          # grid position of textbox

# submit button - Button (9:30 mins) - calls onClickSubmitButton function when clicked
Button(window, text="SUBMIT", width=6, command=onClickSubmitButton ).grid (row=3,column=0, sticky = W)

#definitions - Label (11:50 mins)
Label(window, text="\n Definitions", bg="white", font="none 12 bold").grid(row=4,column=0,sticky=W) # using grid layout

# output textField - Text(12:40 mins)
outputTextField = Text(window, width=75, height=6, wrap=WORD, background="white")
outputTextField.grid(row=4, column=0,sticky=W)  # grid position of textField

# Dictionary (13:40 mins)
# Students ToDo Add 20 python expressions / items to the dictionary - Note last item should not have a ',' at the end
python_dictionary = {
    'algorithm': ' Step by step instructions to complete a task',
    'PhotoImage': ' gif image object that can be displayed by tkinter',
    'variable' : 'a value assigned to a name, which can be changed',
    'string' : 'a sequence of letters, numbers and symbols',
    'integer' : 'a number, positive or negative, with no decimals',
    'float' : 'a number that has decimal places',
    'boolean' : 'a value of true or false',
    'loop' : 'a piece of code that continually runs until a condition is met',
    'tuple' : 'multiple values stored together. they are ordered. they cannot be changed',
    'list' : 'multiple values stored together. they are ordered. these can be changed',
    'dictionary' : 'multiple values organised into a key:value pair. they are not ordered. they can be changed.',
    'function' : 'a piece of code written to perform a set of actions. made to be reused by calling a name'
    }

# exit Labeland Button (17:00 mins) - - calls onClickExitButton function when clicked
Label(window, text="click to exit", bg="white", font="none 12 bold").grid(row=6,column=0,sticky=W) # using grid layout
Button(window, text="Exit", width=14, command=onClickExitButton ).grid (row=7,column=0, sticky = W)

# run the main loop
window.mainloop()
