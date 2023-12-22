def outer() :
    print("In an Outer Function")
    def inner() :
        print("In an Inner Function")
    inner()

outer()

