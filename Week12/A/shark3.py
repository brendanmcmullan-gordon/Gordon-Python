class Shark:
    animalType = "fish"
    location = "ocean"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setFollowers(self, followers):
        print("This user has " + str(followers) + " followers")

def main():

    sammy = Shark("Sammy", 5)
    print(sammy.name)
    print(sammy.location)

    stephan = Shark("Stephan", 8)
    print(stephan.name)
    stephan.setFollowers(77)
    print(stephan.animalType)

    jessica = Shark("Jessica", 4)
    print(jessica.name)
    print(jessica.age)
    jessica.setFollowers(87)

    print("Common attributes: Shark.animalType = " + Shark.animalType + " and Shark.location = " + Shark.location)

if __name__ == "__main__":
    main()
