x1 = input('Enter the x1-coordinate: ')
x2 = input('Enter the x2-coordinate: ')
y1 = input('Enter the y1-coordinate: ')
y2 = input('Enter the y2-coordinate: ')

x1 = float(x1) 
y1 = float(y1)
x2 = float(x2)
y2 = float(y2) 

def slope (x1, y1, x2,y2):
    return (float)(y2-y1)/(x2-x1)

print (f"slope from ({x1},{y1}) and ({x2},{y2}) is {format('%.5f'%slope(x1, y1, x2, y2))}.") 

