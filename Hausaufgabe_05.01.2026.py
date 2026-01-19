def durchdreiteilbare(zahl, teiler):
    if zahl % teiler == 0:
        return True
    return False

for i in range (1,21):
   teilbar = durchdreiteilbare(i, 3)
   # durchdreiteilbare(i, 3)
   # print(durchdreiteilbare(i, 3))
   if teilbar:
       print(i)