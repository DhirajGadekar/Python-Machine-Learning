def multipleValue(a, b, c) :
    a += 10
    b += 20
    c += 30
    return a,b,c

ret = multipleValue(10, 20, 30)
print(type(ret))

for i in ret :
    print(i)

a,b,c = multipleValue(10, 20, 30)
print(a)
print(b)
print(c)

