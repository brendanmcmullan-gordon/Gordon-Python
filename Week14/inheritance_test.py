class Fish:
    def __init__(self, firstName, lastName="Fish"):
        self.firstName = firstName
        self.lastName = lastName

    def swim(self):
        print(self.firstName, "the fish is swimming.")

    def swimBackwards(self):
        print(self.firstName, "the fish can swim backwards.")

class Trout(Fish):
    def __init__(self, water="freshwater"):
        self.water = water
        super().__init__(self)

class Clownfish(Fish):
    def anemone(self):
        print("The clownfish is coexisting with an anemone")

class Shark(Fish):
    def __init__(self, firstName, lastName="Shark", skeleton="cartilage", eyelids=True):
        self.firstName = firstName
        self.lastName = lastName
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swimBackwards(self):
        print(self.firstName, "the shark cannot swim backwards, but can sink backwards.")

# terry = Trout("Terry", "Trout")
# print(terry.firstName, terry.lastName)
# terry.swim()
# terry.swimBackwards()

print()

carrie = Clownfish("Carrie")
print(carrie.firstName, carrie.lastName)
carrie.swim()
carrie.anemone()

print()

sammy = Shark("Sammy")
print(sammy.firstName, sammy.lastName)
sammy.swim()
sammy.swimBackwards()
print(sammy.eyelids)
print(sammy.skeleton)

print()

terry = Trout()
terry.firstName = "Terry"
print(terry.firstName, terry.lastName)
print(terry.water)
terry.swim()
