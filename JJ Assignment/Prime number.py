while True: 

    num = int(input("Enter your number: ")) 

    def prime(num):
        if num > 1:
            for i in range ( 2,num ): 
                if num % i == 0: 
                    return False; 
        else:
            return False
        return True 

    if prime(num): 
        x = str(num)[::-1]
        x = int(x)
        if prime(x):
            print(f"The number {num} as its reverse, {x}, is also a prime number.")
        else: 
            break 
    else: 
        print (f"{num} is False! ")



