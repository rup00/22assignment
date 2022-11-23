def octal(decimal): 
  
    if decimal > 0:  
      
        octal = decimal % 8
        decimal = decimal // 8
        octal(decimal)  
        print(octal, end = "")  
          
decimal = int(input("Enter any decimal number: "))  
octal(decimal)