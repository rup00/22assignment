def oddSum(N): 
    if N <= 0: 
        return 0
    else: 
        return N + oddSum(N - 2)