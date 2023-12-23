def fun() :
    print("Start Fun")
    yield 10
    yield 20
    yield 30
    print("End Fun")

for i in fun():
    print(i)
