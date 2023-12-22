
def decorFun(func) :
    def wrapper(*args):
        print("Start Wrapper")
        val = func(*args)
        print("End Wrapper")
        return val

    return wrapper

@decorFun
def normalFun(x, y):
    print("In normal Fun")
    return x + y

#normalFun = decorFun(normalFun)
print(normalFun(10, 20))
