class Company:
    def disp(self) :
        print(id(self))
        print(type(self))

print("start code")
obj = Company()
obj.disp()
print(id(obj))
print(type(obj))
print("End Code")
