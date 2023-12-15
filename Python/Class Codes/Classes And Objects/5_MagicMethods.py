class Company :
    def __new__(self):
        print("Memory Allocate")
        return object.__new__(self)
    
    def __init__(self):
        print("In Constructor")

obj = Company()
