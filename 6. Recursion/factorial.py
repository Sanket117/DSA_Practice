def factorialNum(num):
    if (num == 0):
        return 1
    return num * factorialNum(num-1)

print(factorialNum(5))