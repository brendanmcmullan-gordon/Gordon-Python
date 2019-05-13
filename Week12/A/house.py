class House:
    type = "dwelling"
    location = "terrestrial"

    def __init__(self, name, material, size, storeys):
        self.name = name
        self.material = material
        self.size = size
        self.storeys = storeys

def main():

    cheapHouse = House("A", "brick", "14sqm", 1)
    print("Name:", cheapHouse.name, "Material:", cheapHouse.material, "Size", cheapHouse.size, "Storeys", cheapHouse.storeys)

    expensiveHouse = House("B", "weatherboard", "17sqm", 2)
    print("Name:", expensiveHouse.name, "Material:", expensiveHouse.material, "Size:", expensiveHouse.size, "Storeys", expensiveHouse.storeys)

if __name__ == "__main__":
    main()
