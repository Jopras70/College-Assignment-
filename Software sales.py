packages = eval(input("Enter the number of packages purchased: "))

if packages < 10: 
    disc = 0
elif 10 <= packages < 20: 
    disc = 10
elif 20 <= packages < 50: 
    disc = 20 
elif 50 <= packages < 100:
    disc = 30 
elif packages >= 100: 
    disc = 40 

price = 99 
pack = packages*price 
discount = (disc/100)*pack
total = pack-discount

print (f"Discount amount @", disc,"%: ${:.2f}".format(discount))
print (f"Total amount: ${format('%.2f'%total)}")