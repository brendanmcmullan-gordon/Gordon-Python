class Dog:
    species = "Canis familaris"

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

def main():
    awoo = Dog("Beagle", "Toby", 3)
    print(awoo.breed, awoo.name, awoo.age)

    bork = Dog("Shiba Inu", "Christopher", 5)
    print(bork.breed, bork.name, bork.age)

    heck = Dog("Irish Wolfhound", "Robert", 1)
    print(heck.breed, heck.name, heck.age)

    print("Common attributes: Dog.species = " + Dog.species)

if __name__ == "__main__":
    main()
