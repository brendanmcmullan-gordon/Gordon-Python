# Name: Brendan McMullan
# ID: 12135005
# Date 29/04/2019

from tkinter import *
from decimal import *
#   Decimal() is used to easily limit decimal places without using a print statement

def twoPlaces(x):
    a = Decimal(x).quantize(Decimal('.01'))
    return a

# Customer Name Entry Submit Button
#   pull the customer's name into a variable
#   go to next window on submit

def getCustName():
    global custName
    custName = userNameEntry.get()
    priceEntryFrame.pack()
    nameEntryFrame.destroy()
    window1.title("BRUNNINGS WAREHOUSE - ITEM PRICE")

# Customer Item Price Entry Submit Button (Repeatable)
#   pull the entered price into a variable
#   sum prices into another variable
#   clear window on click
#
#   go to next window when price entered = 0

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
        totalCostStr.set("%.2f" %totalCost)
        paymentMethodFrame.pack()
        priceEntryFrame.destroy()
        window1.title("BRUNNINGS WAREHOUSE - PAYMENT METHOD")

# Payment Method Submit Button
#   Pull the payment method into a variable and change window
#   depending on what payment method was chosen

def getPaymentMethod():
    global payMethod
    payMethod = str(paymentMethodEntry.get())
    payMethod = payMethod.lower()
    if payMethod == "credit":
        if totalCost < 20.00:
            creditPaymentErrorFrame.pack()
            paymentMethodFrame.destroy()
            window1.title("BRUNNINGS WAREHOUSE - ERROR - CREDIT PAYMENT MINIMUM")
        else:
            creditPaymentFrame.pack()
            paymentMethodFrame.destroy()
            window1.title("BRUNNINGS WAREHOUSE - CREDIT PAYMENT - PROCESSING")
    elif payMethod == "cash":
        cashPaymentFrame.pack()
        paymentMethodFrame.destroy()
        window1.title("BRUNNINGS WAREHOUSE - CASH PAYMENT")
    else:
        paymentMethodEntry.delete(0, END)
        paymentMethodEntry.insert(0, "Invalid Method")

# Used to switch from the credit error frame to the cash frame

def switchToCashPayment():
    cashPaymentFrame.pack()
    creditPaymentErrorFrame.destroy()
    window1.title("BRUNNINGS WAREHOUSE - CASH PAYMENT")

# Used to switch to the credit payment success frame

def progressCreditPayment():
    global custName
    custNameStr.set(custName)
    creditPaymentSuccessFrame.pack()
    creditPaymentFrame.destroy()
    window1.title("BRUNNINGS WAREHOUSE - CREDIT PAYMENT - SUCCESS")

# Used to get the cash given and calculate the change

def getCash():
    global cashGiven
    global cashChange
    global totalCost
    global custName
    custNameStr.set(custName)
    try:
        cashGiven = float(cashPaymentEntry.get())
        cashChange = cashGiven - totalCost
        cashChangeStr.set("%.2f" %cashChange)
        cashPaymentSuccessFrame.pack()
        cashPaymentFrame.destroy()
        window1.title("BRUNNINGS WAREHOUSE - CASH PAYMENT - SUCCESS")
    except ValueError:
        pass


# exit the program

def exitFunc():
    exit()

# Windows needed:
#   Enter name window
#   Item price entry window
#   Total + Method of payment window
#   Cash + Credit payment window

# Main TKinter window
window1 = Tk()

# Variables
custName = ""
custNameStr = StringVar()
itemPrice = None
totalCost = 0.0
totalCostStr = StringVar()
payMethod = ""
cashGiven = 0.0
cashChange = 0.0
cashChangeStr = StringVar()

# 'standard' window colour
appColour = "#007047"

#
#       change window title on window change w/ functions
#

window1.title("BRUNNINGS WAREHOUSE - ENTER NAME")
window1.config(bg=appColour)

#
#   *** FRAMES ***
#

# First window frame - Name entry
nameEntryFrame = Frame(window1,
                       bg=appColour)
nameEntryFrame.pack(ipadx=5,
                    ipady=5)

# Second window frame - Item cost entry
priceEntryFrame = Frame(window1,
                        bg=appColour)

# Third window frame - Payment method entry
# has a secondary frame - paymentMethodTotalFrame
paymentMethodFrame = Frame(window1,
                           bg=appColour)

# Fourth window frame - Credit payment error

creditPaymentErrorFrame = Frame(window1,
                           bg=appColour)

# Fifth window frame - Credit payment

creditPaymentFrame = Frame(window1,
                           bg=appColour)

# Sixth window frame - Credit payment success

creditPaymentSuccessFrame = Frame(window1,
                                  bg=appColour)

# Seventh window frame - Cash payment

cashPaymentFrame = Frame(window1,
                         bg=appColour)

# Eighth window frame - Cash payment success
# has a secondary frame - cashPaymentSuccessTopFrame

cashPaymentSuccessFrame = Frame(window1,
                                bg=appColour)

#
#   *** FRAME ELEMENTS ***
#

# ===== Customer Name Entry Window Elements =====

nameEntryLabel = Label(nameEntryFrame,
                       text="Please enter your name:",
                       font="none 20",
                       bg=appColour,
                       fg="white")
nameEntryLabel.pack(side=LEFT)

userNameEntry = Entry(nameEntryFrame,
                      width=10,
                      bg="white",
                      font="none 20")
userNameEntry.pack(side=LEFT, padx=10, pady=10)

nameEntryButton = Button(nameEntryFrame,
                         text="SUBMIT",
                         width=6,
                         command=getCustName)
nameEntryButton.pack(side=LEFT)

# ===== Price Entry Window Elements =====

priceEntryLabel = Label(priceEntryFrame,
                        text="Please enter the price of your item (dd.cc):",
                        font="none 20",
                        bg=appColour,
                        fg="white")
priceEntryLabel.pack(side=LEFT)

priceEntryLabel2 = Label(priceEntryFrame,
                         text="Enter '0' to finish.",
                         font="none 16",
                         bg=appColour,
                         fg="white")
priceEntryLabel2.pack(side=BOTTOM)

priceEntry = Entry(priceEntryFrame,
                   width=6,
                   bg="white",
                   font="none 20")
priceEntry.pack(side=LEFT, padx=10, pady=10)

priceEntryButton = Button(priceEntryFrame,
                          text="SUBMIT",
                          width=6,
                          command=getPrice)
priceEntryButton.pack(side=LEFT)

# ===== Payment Method Window Elements =====

paymentMethodTotalFrame = Frame(paymentMethodFrame)
paymentMethodTotalFrame.pack()

paymentMethodTotal1 = Label(paymentMethodTotalFrame,
                            text="Your total is: $",
                            font="none 20",
                            bg=appColour,
                            fg="white")
paymentMethodTotal1.pack(side=LEFT)

paymentMethodTotal2 = Label(paymentMethodTotalFrame,
                            textvariable=totalCostStr,
                            font="none 20",
                            bg=appColour,
                            fg="white")
paymentMethodTotal2.pack()

paymentMethodLabel = Label(paymentMethodFrame,
                           text="Please enter your method of payment (Cash/Credit):",
                           font="none 20",
                           bg=appColour,
                           fg="white")
paymentMethodLabel.pack()

paymentMethodEntry = Entry(paymentMethodFrame,
                           font="none 20",
                           width=20,
                           bg="white")
paymentMethodEntry.pack(side=LEFT, padx=100)

paymentMethodButton = Button(paymentMethodFrame,
                             text="SUBMIT",
                             width=6,
                             command=getPaymentMethod)
paymentMethodButton.pack(side=LEFT, padx=10)

# ===== Credit Payment Error Window Elements =====

creditPaymentErrorLabel = Label(creditPaymentErrorFrame,
                                text="Attention: This payment is less than $20.00 and will be processed as a cash payment.",
                                font="none 20",
                                bg=appColour,
                                fg="white")
creditPaymentErrorLabel.pack()

creditPaymentErrorButton = Button(creditPaymentErrorFrame,
                                  text="OK",
                                  width=3,
                                  command=switchToCashPayment)
creditPaymentErrorButton.pack()

# ===== Credit Payment Window Elements =====

creditPaymentLabel = Label(creditPaymentFrame,
                           text="Processing your payment...",
                           font="none 20",
                           bg=appColour,
                           fg="white")
creditPaymentLabel.pack()

creditPaymentButton = Button(creditPaymentFrame,
                             text="OK",
                             width=3,
                             command=progressCreditPayment)
creditPaymentButton.pack()

# ===== Credit Payment Success Window Elements =====

creditPaymentSuccessLabel = Label(creditPaymentSuccessFrame,
                            text="Your payment has been processed! \n Thanks for shopping at BRUNNINGS,",
                            font="none 20",
                            bg=appColour,
                            fg="white")
creditPaymentSuccessLabel.pack(side=LEFT)

creditPaymentSuccessLabelName = Label(creditPaymentSuccessFrame,
                                textvariable=custNameStr,
                                font="none 20",
                                bg=appColour,
                                fg="white")
creditPaymentSuccessLabelName.pack(side=LEFT, anchor="s")

creditPaymentSuccessButton = Button(creditPaymentSuccessFrame,
                             text="OK",
                             width=3,
                             command=exitFunc)
creditPaymentSuccessButton.pack(padx=10, side=RIGHT)

# ===== Cash Payment Window Elements =====
cashPaymentTopFrame = Frame(cashPaymentFrame)
cashPaymentTopFrame.pack()

cashPaymentLabel = Label(cashPaymentTopFrame,
                         text="Please enter the amount of cash you are paying with (dd.cc)",
                         font="none 20",
                         bg=appColour,
                         fg="white")
cashPaymentLabel.pack()

cashPaymentEntry = Entry(cashPaymentFrame,
                         font="none 20",
                         width=20,
                         bg="white")
cashPaymentEntry.pack(padx=125, side=LEFT)

cashPaymentButton = Button(cashPaymentFrame,
                           text="SUBMIT",
                           width=6,
                           command=getCash)
cashPaymentButton.pack(padx=10, side=LEFT)

# ===== Cash Payment Success Window Elements =====

cashPaymentSuccessTopFrame = Frame(cashPaymentSuccessFrame)
cashPaymentSuccessTopFrame.pack()


cashPaymentSuccessChangeLabel1 = Label(cashPaymentSuccessTopFrame,
                                text="Your change is: $",
                                font="none 20",
                                bg=appColour,
                                fg="white")
cashPaymentSuccessChangeLabel1.pack(side=LEFT)

cashPaymentSuccessChangeLabel1 = Label(cashPaymentSuccessTopFrame,
                                textvariable=cashChangeStr,
                                font="none 20",
                                bg=appColour,
                                fg="white")
cashPaymentSuccessChangeLabel1.pack(side=LEFT)

cashPaymentSuccessLabel = Label(cashPaymentSuccessFrame,
                                text="Thanks for shopping at BRUNNINGS,",
                                font="none 20",
                                bg=appColour,
                                fg="white")
cashPaymentSuccessLabel.pack(side=LEFT)

cashPaymentSuccessLabelName = Label(cashPaymentSuccessFrame,
                                    textvariable=custNameStr,
                                    font="none 20",
                                    bg=appColour,
                                    fg="white")
cashPaymentSuccessLabelName.pack(side=LEFT)

cashPaymentSuccessButton = Button(cashPaymentSuccessFrame,
                                  text="OK",
                                  width=3,
                                  command=exitFunc)
cashPaymentSuccessButton.pack(padx=10, pady=10)

window1.mainloop()
