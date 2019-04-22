from tkinter import *

# pull the customer's name into a variable
# go to next window on submit
def getCustName():
    global custName
    custName = userNameEntry.get()
    priceEntryFrame.pack()
    nameEntryFrame.destroy()

# pull the entered price into a variable
# sum prices into another variable
# clear window on click
#
# go to next window when price entered = 0
def getPrice():
    global itemPrice
    global totalCost
    try:
        itemPrice = float(priceEntry.get())
        totalCost += itemPrice
        priceEntry.delete(0, END)
    except ValueError:
        pass
    if itemPrice == 0:
        totalCostStr.set(totalCost)
        paymentMethodFrame.pack()
        priceEntryFrame.destroy()


# Pull the payment method into a variable and change window
# depending on what payment method was chosen

def getPaymentMethod():
    pass

# Windows needed:
    # Enter name window
    # Item price entry window
    # Total + Method of payment window
    # Cash/Credit payment window

# Main TKinter window
window1 = Tk()

# Variables
itemPrice = None
totalCost = 0.0
totalCostStr = StringVar()
payMethod = ""
cashGiven = 0.0
cashChange = 0.0

appColour = "#007047"

#
#       change window title on window change w/ functions
#
window1.title("BRUNNINGS WAREHOUSE - ENTER NAME")
window1.config(bg=appColour)

# First window frame
nameEntryFrame = Frame(window1,
                       bg=appColour)
nameEntryFrame.pack(ipadx=5,
                    ipady=5)

# Second window frame
priceEntryFrame = Frame(window1,
                        bg=appColour)

# Third window frame
paymentMethodFrame = Frame(window1,
                           bg=appColour)

#no pack here; goes in function

#TKinter frames
# topFrame = Frame(nameEntryFrame)
# topFrame.pack(expand=1)
#
# midFrame = Frame(nameEntryFrame)
# midFrame.pack(expand=1)
#
# botFrame = Frame(nameEntryFrame)
# botFrame.pack(expand=1,
#               side=BOTTOM)

# ===== Customer Name Entry Window Elements =====

nameEntryLabel = Label(nameEntryFrame,
                       text="Please enter your name:",
                       font="none 24",
                       bg=appColour,
                       fg="white")
nameEntryLabel.pack(side=LEFT)

userNameEntry = Entry(nameEntryFrame,
                      width=10,
                      bg="white",
                      font="none 24")
userNameEntry.pack(side=LEFT, padx=10, pady=10)

nameEntryButton = Button(nameEntryFrame,
                         text="SUBMIT",
                         width=6,
                         command=getCustName)
nameEntryButton.pack(side=LEFT)

# ===== Price Entry Window Elements =====

priceEntryLabel = Label(priceEntryFrame,
                        text="Please enter the price of your item (dd.cc):",
                        font="none 24",
                        bg=appColour,
                        fg="white")
priceEntryLabel.pack(side=LEFT)

priceEntry = Entry(priceEntryFrame,
                   width=6,
                   bg="white",
                   font="none 24")
priceEntry.pack(side=LEFT, padx=10, pady=10)

priceEntryButton = Button(priceEntryFrame,
                          text="SUBMIT",
                          width=6,
                          command=getPrice)
priceEntryButton.pack(side=LEFT)

# ===== Method of Payment Window Elements =====
paymentMethodTotalFrame = Frame(paymentMethodFrame)
paymentMethodTotalFrame.pack()

paymentMethodTotal1 = Label(paymentMethodTotalFrame,
                            text="Your total is: $",
                            font="none 16",
                            bg=appColour,
                            fg="white")
paymentMethodTotal1.pack(side=LEFT)

paymentMethodTotal2 = Label(paymentMethodTotalFrame,
                            textvariable=totalCostStr,
                            font="none 16",
                            bg=appColour,
                            fg="white")
paymentMethodTotal2.pack()

paymentMethodLabel = Label(paymentMethodFrame,
                           text="Please choose your method of payment (Cash/Credit):",
                           font="none 16",
                           bg=appColour,
                           fg="white")
paymentMethodLabel.pack()

paymentMethodEntry = Entry(paymentMethodFrame,
                           font="none 24",
                           width=10,
                           bg="white")
paymentMethodEntry.pack(side=LEFT, padx=100)

paymentMethodButton = Button(paymentMethodFrame,
                             text="SUBMIT",
                             width=6,
                             command=getPaymentMethod)
paymentMethodButton.pack(side=LEFT)
#
# Make an entry for price
#

window1.mainloop()
