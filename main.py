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

sar1=[5,2,1,2,1,12]
reizinajums=1
for elem in sar1:
  print("tekosais elements=", elem, "tekosais reizinajums=", reizinajums)
  reizinajums=reizinajums*elem
print("Reizinajums=", reizinajums)

a = input()
a = int(a)
para = 0
nepara = 0
while a > 0:
    if a % 2 == 0:
        para += 1
    else:
        nepara += 1
    a = a // 10
 
print("para: %d, nepara: %d" % (para, nepara))

sar1=[5,2,1,2,1,12,67,87]
reizinajums=1
summa=0
for elem in sar1:
  print("tekosais elements=", elem, "tekosais reizinajums=", reizinajums)
  reizinajums=reizinajums*elem
  if elem%2==0:
    summa+=elem
print("Reizinajums=", reizinajums)
print("summa=", summa)

sar1=[5,2,1,2,1,12]
reizinajums=1
for elem in sar1:
  print("Tekosais elements =", elem,
   " Tekojais reizinajums =",
reizinajums)
reizinajums=reizinajums*elem
print("Reizinajums =", reizinajums)
summa=sum(sar1)
print(summa)

sar1=[5,45,1,2,1, 12]
reizinajums=1
for elem in sar1:
reizinajums=reizinajums*elem
print ("Reizinäjums =", reizinajums)
summa=sum(sar1)
print(summa)



skait=0
while skait<=100:
if skait%2==0:
   print(skait)
skait+=1