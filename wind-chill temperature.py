tempt = eval(input("Enter the temperature in fahrenheit: "))

while True:
    if tempt < -58 or tempt > 41:
        print("Temperature must be between -58F and 41F")
        tempt = eval(input("Please re-enter the temperature in Fahrenheit: "))
    else:
        break 

windspeed = eval(input("Enter the wind speed miles per hour: "))

while True: 
    if windspeed <= 2: 
        print("Speed must be greater than or equal to 2")
        windspeed = eval(input("Please re-enter the wind speed miles per hour: "))
    else:
        break

windchill = 35.74 + (0.6215*tempt) - (35.75*(windspeed**0.16)) + (0.4275*tempt*(windspeed**0.16))

print(f"The wind chill index is {format('%.3f'%windchill)}")


