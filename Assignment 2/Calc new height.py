def calc_new_height (): 
    width = eval(input("Enter the current width: "))
    height = eval(input("Enter the current height: "))
    desired = eval(input("Enter the desired width: "))
    
    while desired > width: 
        desired = eval(input("Please re-enter the desired width, desired width must be smaller than the current width: "))
    
    hasil = height / (width/desired)

    print (f"The corresponding height is: {hasil}")

calc_new_height()

