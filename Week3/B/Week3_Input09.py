#Enter two doubles representing the length and width of a rectangle. Calculate and display (1) the area and (2) the perimeter.

widthStr = int(input("Please enter the width of the rectangle in metres."))
heightStr = int(input("Please enter the height of the rectangle in metres."))

print("The area of the rectangle is", widthStr*heightStr, "sq metres.")
print("The perimeter of the rectangle is", (widthStr*2)+(heightStr*2), "metres.")
