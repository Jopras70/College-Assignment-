from Restoran import RestoJo

def ShopListJo():
    #create list
    shop = [];
    #user prompt to input Number of Items
    n = int(input('Please Input Number of Items you buy :'))

    #creating list of object
    for i in range(n):
        #input name of Items
        name = input('Items Name :')

        #input and validate items weight
        x = -1;
        while x<0:
            x = int(input('Input Weight :'))
        
        #create object and append to list
        newItems = RestoJo(name, x)
        shop.append(newItems)
    #return list of object
    return shop

def DisplayListJo(shop):
    for item in shop:
        print(item.name, "             ", item.weight)
        print("                  ", item.CalcPrice())

def TotalPayment(shop):
    sum = 0.00
    for item in shop:
        sum += item.CalcPrice()
    return sum


def main():
    #call all function

    #call function ShopListJo() to create Object shop and store in list shops
    shops = ShopListJo()

    #Display list
    DisplayListJo(shops)

    #print total Payment
    print(TotalPayment(shops))

main()