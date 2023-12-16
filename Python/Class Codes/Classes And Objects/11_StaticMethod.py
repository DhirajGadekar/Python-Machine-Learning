class Player :
    teamName = "India"
    def __init__(self, jerNo, pName) :
        self.jerNo = jerNo
        self.pName = pName

    @staticmethod
    def playerInfo() :
        print(Player.teamName)

cricPlayer = Player(45, "Rohit")

Player.playerInfo()
cricPlayer.playerInfo()
