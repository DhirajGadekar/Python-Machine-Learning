def decorfun(func) :
    def wrapper() :
        print("Start Wrapper");
        func()
        print("End Wrapper")
    return wrapper;

def normalFun() :
    print("Hello in Normal Function");

normalFun = decorfun(normalFun)
normalFun()
