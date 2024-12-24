def printNum(num):
    if (num == 0):
        return 0
    print(num)    
    res = printNum(num-1)
    
    return res
    
print(printNum(5))