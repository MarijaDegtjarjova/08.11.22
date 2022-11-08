teksts=input("ievadi tekstu!")
skaititajs=0
for burts in teksts:
  if burts=='c':
    skaititajs+=1
print("Burtu c skaits =",skaititajs)


sar1=[5,46,1,0,45,12]
garums=len(sar1)
lielakais=max(sar1)
mazakais=min(sar1)
atkartojumi=sar1.count(45)
print(atkartojumi)