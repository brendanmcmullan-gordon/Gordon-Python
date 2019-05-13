class Tree:
    def __init__(self, name, fruit):
        self.name = name
        self.fruit = fruit

    def oil(self):
        print("This plant can be used in the production of essential oils")

class Eucalyptus(Tree):
    def oil(self):
        print("This plant has volatile essential oils")

class Pear(Tree):
    def beverage(self):
        print("Pears can be used to make pear cider")


euc = Eucalyptus("Euc", "Leaves")
print(euc.name, euc.fruit)
euc.oil()

pear = Pear("P", "Pears")
print(pear.name, pear.fruit)
pear.oil()
pear.beverage()
