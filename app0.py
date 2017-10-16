import random

dizi=[]
Sdizi=[]
var=[]
sayac=1

for x in range(0,10):
    i=random.randint(1,9)
    dizi.append(i)
    print (dizi[x])

for i in range(0,10):
    vardir=0
    for k in range(len(var)):
        if(var[k]==dizi[i]):
            vardir=1
            break
            
    if(vardir==0):
        var.append(dizi[i])
        print(var)
        
        sayac=1
        for j in range(0,10):
            if(i!=j):
                if(dizi[i]==dizi[j]):
                    sayac=sayac+1
        
        Sdizi.append(str(dizi[i])+':'+str(sayac))

print(Sdizi)
