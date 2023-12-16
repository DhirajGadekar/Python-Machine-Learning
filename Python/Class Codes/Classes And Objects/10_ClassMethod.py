class Player :
    teamName = "India"
    def __init__(self, jerNo, pName) :
        print(self)
        self.jerNo = jerNo
        self.pName = pName
    
    @classmethod
    def playerInfo(cls) :
        print(cls)
        print(cls.teamName)

cricPlayer1 = Player(45, "Rohit")
cricPlayer1 = Player(18, "Virat")

cricPlayer1.playerInfo()
