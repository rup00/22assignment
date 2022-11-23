
def squares(n): 
    if n <= 0: 
        return 0
    else: 
        return n*n + squares(n-1)