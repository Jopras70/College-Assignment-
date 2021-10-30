x = eval(input("Enter the number of height: "))

for i in range (x):
    print ( " " * ( x-i ) + " $" * ( i+1 ))

for j in range (x-1):
    print ( " " * (j+2) + " $" * ( x-1-j ))


