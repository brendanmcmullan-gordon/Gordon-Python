class Sport:
    activity = "physical"
    games = "competitive"

    def __init__(self, name, numPlayers, ballShape):
        self.name = name
        self.numPlayers = numPlayers
        self.ballShape = ballShape

def main():

    tennis = Sport("tennis", 2, ("small", "round"))
    print(tennis.name, tennis.numPlayers, tennis.ballShape[0], tennis.ballShape[1])

    soccer = Sport("soccer", 22, ("large", "round"))
    print(soccer.name, soccer.numPlayers, soccer.ballShape[0], soccer.ballShape[1])

    AFL = Sport("AFL", 18, ("large", "oval"))
    print(AFL.activity, AFL.games, AFL.name, AFL.numPlayers, AFL.ballShape[0], AFL.ballShape[1])


if __name__ == "__main__":
    main()
