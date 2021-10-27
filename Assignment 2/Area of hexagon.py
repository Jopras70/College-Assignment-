import math 

sidelength = eval(input("Enter the side length of the hexagon: ")) 

area = (3*math.sqrt(3)/2)*(math.pow(sidelength,2))

print (f"The area of a hexagon with side length {sidelength} is {format('%.3f'%area)}")

