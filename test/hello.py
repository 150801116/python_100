import random
with open("E:/sts-2.1.2/data/output.txt","w") as f:
  j=1
  for i in range(100000000):
    number=random.randint(0,1)
    if j==25:
        text = f.write(str(number) + "\n")
        j = 0
    else:
        text = f.write(str(number))
    j=j+1


f.close()