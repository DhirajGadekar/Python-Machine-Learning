class Employee :

    def __init__(self) :
        print("In Constructor")
        self.x = 10
        self.y = 20

    def disp(self) :
        print(self.x)
        print(self.y)

emp = Employee()
emp.disp()
