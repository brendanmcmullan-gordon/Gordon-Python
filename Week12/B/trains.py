class Train:
    substrate = "Track"

    def __init__(self, fuelType, cargo, numCarriages):
        self.fuelType = fuelType
        self.cargo = cargo
        self.numCarriages = numCarriages

def main():

    passengerTrain = Train("Electric", "People", 10)
    print(passengerTrain.fuelType, passengerTrain.cargo, passengerTrain.numCarriages)

    freightTrain = Train("Diesel", "Containers", 20)
    print(freightTrain.fuelType, freightTrain.cargo, freightTrain.numCarriages)

    steamTrain = Train("Steam", "Coal", 5)
    print(steamTrain.fuelType, steamTrain.cargo, steamTrain.numCarriages)



if __name__ == "__main__":
    main()
