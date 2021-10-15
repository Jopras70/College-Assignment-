edge1 = eval(input("Enter length of edge1: "))
edge2 = eval(input("Enter length of edge2: "))
edge3 = eval(input("Enter length of edge3: "))

perimeter = edge1+edge2+edge3

if (edge1+edge2 >= edge3) and (edge2+edge3 >= edge1) and (edge1+edge3 >= edge2):
    print (f"The perimeter is: {perimeter}")
else:
     print ("Perimeter cannot be calculated: the input is invalid.")

     