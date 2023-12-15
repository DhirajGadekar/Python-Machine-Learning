def fun():
    print("In Fun")

def fun(x):
    print("In fun - x")

fun()
fun(10)

#TypeError: fun() missing 1 required positional argument: 'x'
