def fun() :
    return 10

def run() :
    yield 10
    yield 20

ret = fun()
gen = run()

print(type(ret))
print(type(gen))

print(next(gen));
print(next(gen));
# print(next(gen));  Error : StopIteration
