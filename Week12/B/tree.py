class Tree:
    kingdom = "Plantae"

    def __init__(self, type, height, location):
        self.type = type
        self.height = height
        self.location = location


def main():
    bigTree = Tree("Eucalyptus", 10, "My Backyard")
    print("This is a", bigTree.type, "tree, It is", bigTree.height, "Meters Tall, and is located in", bigTree.location)

    smallTree = Tree("Birch", 15, "a Forest")
    print("This is a", smallTree.type, "tree, It is", smallTree.height, "Meters Tall, and is located in", smallTree.location)

    oldTree = Tree("Pine", 8, "another Forest")
    print("This is a", oldTree.type, "tree, It is", oldTree.height, "Meters Tall, and is located in", oldTree.location)

if __name__ == "__main__":
    main()
