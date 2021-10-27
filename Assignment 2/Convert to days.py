def convert_to_days(): 
    hours = eval(input("Enter number of hours: "))
    minutes = eval(input("Enter number of minutes: "))
    seconds = eval(input("Enter number of seconds: "))

    answer = get_days(hours,minutes,seconds)

    print (f"The number of days is: {answer}")

def get_days(hours=int, minutes=int, seconds=int): 
    day = ((seconds / 3600) + (minutes / 60) + hours) / 24 

    return round (day,4)

convert_to_days()

