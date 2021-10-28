import random

randomint = random.randint(1, 100)
chance = 50 
while chance > 0: 
    data = int(input("Enter your number you choose: "))
    if data > randomint: 
        chance -= 1 
        print ("The number you choose is bigger")
    
    if data < randomint:
        chance -= 1 
        print ("The number you choose is smaller")
    
    if data == randomint: 
        chance -= 1 
        print ("Congratulation your answer is right")

        