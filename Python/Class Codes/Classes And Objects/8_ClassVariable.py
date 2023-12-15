class Company :
    compName = "Facebook"
    def __init__(self) :
        print("In Constructor")
        self.empId = 12
        self.empName = "Kanha"

    def compInfo(self) :
        print(self.empId)
        print(self.empName)
        print(self.compName)
        print(Company.compName)
        
emp = Company()
emp.compInfo()
