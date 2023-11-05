def outer() :
    def inner1() :
        print("In inner 1")

    def inner2() :
        print("In inner 2")
        inner1()
    inner2()
outer()
