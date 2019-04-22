def cpuMake(model):
    if model in ("i9", "i7", "i5"):
        if model == "i9":
            size = "14nm"
            make = "Intel"
        if model == "i7":
            size = "22nm"
            make = "Intel"
        print("The", model, "is made by", make, "and has a size of", size)
        return size, make
    else:
        return "Please enter a valid CPU model"

print(cpuMake("i9"))
print(cpuMake("i7"))
