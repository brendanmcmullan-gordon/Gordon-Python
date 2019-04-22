mother = "Jane"
father = "John"
brother = "Joe"
sister = "Jill"

def showFamily(mother, father, brother, sister):
    print(" Family  ")
    print(" ", mother, "    ")
    print(" ", father, "    ")
    print(" ", brother, "    ")
    print(" ", sister, "    ")

def showParents(mother, father):
    print(" Parents  ")
    print(" ", mother, "    ")
    print(" ", father, "    ")

def showSiblings(brother, sister):
    print(" Siblings  ")
    print(" ", brother, "    ")
    print(" ", sister, "    ")

showFamily(mother, father, sister, brother)
showParents(mother, father)
showSiblings(sister, brother)
