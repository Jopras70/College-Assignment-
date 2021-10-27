def calc_weight_on_planet (weight, gravity=23.1):
    mass = weight / 9.8 
    weightonplanet = mass * gravity 

    print (weightonplanet)

calc_weight_on_planet(120, 9.8)

