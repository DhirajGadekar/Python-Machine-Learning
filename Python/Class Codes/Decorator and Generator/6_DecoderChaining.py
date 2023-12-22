def decorFun(func) :
    def wrapper():
        print("Start Wrapper 1")
        func()
        print("End  Wrapper 1")
    return wrapper

def decorRun(func) :
    def wrapper():
        print("Start Wrapper 2")
        func()
        print("End  Wrapper 2")
    return wrapper

def normalFun() :
    print("In Normal Fun")

normalFun = decorFun(decorRun(normalFun))
normalFun()
