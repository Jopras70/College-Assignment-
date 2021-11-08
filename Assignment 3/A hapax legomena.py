import string 

file = open ("text.txt",'r')
text = file.read().lower().replace("\n","")
newtext = ""

for i in text: 
    if i not in string.punctuation:
        newtext += i
text = newtext
last = text.split(" ")
b = {}

for j in last:
    if j not in b: 
        b[j] = 1
    else:
        b[j] += 1 

newb = []

for j in b: 
    if b[j] == 1: 
        newb.append(j) 
print ("These are the hepaxes found in the text: ")
for word in newb:
    print (word)
