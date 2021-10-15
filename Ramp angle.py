import math 

mass = eval(input("Enter the mass of the cart (in kg): "))
force = eval(input("Enter the force to push the cart (in N): "))

g = 9.8 
angle = math.sinh(force/(mass*g))
degree = math.degrees(angle)

print (f"The angel of the ramp is {format('%.1f'%degree)} degrees")

