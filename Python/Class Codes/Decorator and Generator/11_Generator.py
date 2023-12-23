def fun(x, y) :

    print("Start Fun")
    while(x <= y) :
        yield x
        x += 1
    print("End Fun")

for i in fun(1, 10) :
    print(i)
