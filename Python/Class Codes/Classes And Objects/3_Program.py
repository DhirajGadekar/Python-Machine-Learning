def fun(x):
    print("In Fun")

def fun():
    print("In fun - x")

fun()
fun(10)

#O/P:
#In fun - x
#TypeError: fun() missing 1 required positional argument: 'x'
