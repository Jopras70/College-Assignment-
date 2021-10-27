def convert_temperature ():
    fahren = eval(input("Enter the temperature in fahrenheit: "))

    celcius = (5 / 9) * (fahren - 32)
    kelvin = celcius + 273.15 

    print (f"The temperature in fahrenheit is: {fahren}")
    print (f"The temperature in celcius is: {celcius}")
    print (f"The temperature in kelvin is: {kelvin}")

convert_temperature() 

