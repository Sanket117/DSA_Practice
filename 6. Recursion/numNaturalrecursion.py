def sumofNatural(n):
    
    if n ==1:
        return 1
    return n + sumofNatural(n-1)
    
    
    
print(sumofNatural(5))
print(sumofNatural(10))