def sumOfDigits(num): 
    if num == 0: 
         return 0
    return num%10 + sumOfDigits(num//10)