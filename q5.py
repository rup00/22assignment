def sumOfSeries(n): 
    if n < 0: 
        print("Enter a positive number") 
    else: 
        sum = 0
        for i in range(1, n + 1): 
            sum += i * i*i 
              
        return sum