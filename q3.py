def even_sum(n): 
    if n <= 0: 
        return 0
    else: 
        return n + even_sum(n - 2)