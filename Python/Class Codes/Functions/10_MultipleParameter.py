def fun(x, y, **args) :
    print(x)
    print(y)
    for key, value in args.items() :
        print(key, value, sep = ":")

fun(10, 20, a = 30, b = 40, c = 50)
