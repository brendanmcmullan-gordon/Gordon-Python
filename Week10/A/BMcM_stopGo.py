def stopGo(light):
    if light == "go":
        return "green"
    elif light == "stop":
        return "red"
    else:
        return "Please try again"

print(stopGo("go"))
print(stopGo("stop"))
print(stopGo("halt"))
