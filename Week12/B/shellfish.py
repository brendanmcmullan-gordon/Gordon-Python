class Shellfish:
    location = "ocean"
    skeleton = "exoskeleton"

    def __init__(self, shape, type):
        self.shape = shape
        self.type = type

def main():
    snail = Shellfish("spiral", "snail")
    print(snail.shape, snail.type)

    scallop = Shellfish("flat-plates", "scallop")
    print(scallop.location, scallop.shape, scallop.type)

if __name__ == "__main__":
    main()
