import math 

a = int(input("Enter the nemurator, value must be greater than 0: "))
while True: 
    if a < 0 :
        a = int(input("Please re-enter the nemurator, value must be greater than 0: "))
    else :
        break

b = int(input("Enter the denominator, value must be greater than 0: ")) 
while True: 
    if b < 0 : 
        b = int(input("Please re-ennter the denominator, value must be greater than 0: "))
    else : 
        break 

gcd = math.gcd(a, b)
x = a // gcd;  y = b // gcd

if a > b : 
    print (f"{a}/{b} is an improper function")
    if gcd == 1 :
        print ("This improper function can't be reduce further")
        if x%y != 0 :
            print (f"The mixed number is {x//y} and {x%y}/{y}")
        else : 
            print (f"The whole number is {x//y}")
    else : 
        print (f"This improper function can be reduce to: {x}/{y}")
        if x%y != 0 :
            print (f"The mixed number is {x//y} and {x%y}/{y}")
        else : 
            print (f"The whole number is {x//y}")

if a < b :
    print (f"{a}/{b} is an proper function")
    if gcd == 1 : 
        print ("This proper function can't be reduce further")
    else : 
        print (f"This proper function can be reduce to: {x}/{y}")
        
        
