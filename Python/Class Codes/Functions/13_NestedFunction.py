def outer() :

    def inner() :
        print("In inner function")
    return inner

retfun = outer()
print(type(retfun))
retfun()
