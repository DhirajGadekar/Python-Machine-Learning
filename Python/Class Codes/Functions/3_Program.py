def SumOfN(n:int) :
    sum = 0
    for i in range(1, n + 1) :
        sum += i
    return sum

ret = SumOfN(10)
print(ret)
