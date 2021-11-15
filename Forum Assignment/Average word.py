with open('text.txt', 'r') as f:
  x = f.readlines()
  y = 1
  sum = 0
  count = 0
  for i in x:
      j = i.lstrip()
      z = j.split(" ")
      w = i.split(" ")
      if (len(z)>1):
        count += len(z)
        print(z)
        print(len(z))
      for a in w:
          for b in a:
              sum += 1
  #count = count - len(x)
  sum = sum - len(x)
  print(sum/count)
  print(count)
  print(sum)