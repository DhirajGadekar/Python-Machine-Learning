class Company :
    compName = "Facebook"

    def __init__(self) :
        print("In constructor")

    def compInfo(self) :
        print(self.compName)

emp1 = Company()
emp2 = Company()

emp1.compInfo()
emp2.compInfo()

emp1.compName = "Meta"

emp1.compInfo()
emp2.compInfo()

Company.compName = "Meta"

emp1.compInfo()
emp2.compInfo()
