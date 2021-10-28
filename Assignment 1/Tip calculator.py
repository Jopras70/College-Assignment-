subtotal = eval(input("Enter the subtotal: $"))
tipamount = eval(input("Enter tip amount (as a %): "))

tip = subtotal*tipamount/100 
total = subtotal+tip 

print (f"Subtotal: ${subtotal:,.2f}")
print (f"Tip: ${tip:,.2f}")
print (f"Total: ${total:,.2f}")

