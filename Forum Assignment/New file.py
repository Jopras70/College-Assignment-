with open('text.txt', 'r') as f:
    file = open('text1.txt', 'w')
    x = f.readlines()
    y = 1
    for i in x:
        file.writelines([str(y), " ", i]  )
        y += 1  
    file.close()
    