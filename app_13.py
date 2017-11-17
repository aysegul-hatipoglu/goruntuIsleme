import matplotlib.pyplot as plt
import numpy as np
pwd
img_1=plt.imread("b1.jpg")
img_1.ndim
img_1.shape
plt.imshow(img_1)
plt.show()
import os
lista=[]
listb=[]
listc=[]
listd=[]
for i in os.listdir(): #parantez içine dosya uzantısı yazmayınca varsayılan dizinde işlem yapar
    if i.endswith('.jpg'):
        if i[0]=='a1':
            lista.append(i)
            #print(i)
        if i[0]=='b1':
            listb.append(i)
            #print(i)
        if i[0]=='c1':
            listc.append(i)
            #rint(i)
        if i[0]=='d1':
            listd.append(i)
            #print(i)

print(lista)
print(listb)
print(listc)
print(listd)

##DENEME
img_1=plt.imread(lista[0])
img_1.ndim
img_1.shape
#plt.imshow(img_1)
#plt.show()
def resimleri_BW_yapma_center_bulma(liste):
    for i in range(len(liste)):
        img_1=plt.imread(liste[i])
        img_1.ndim
        img_1.shape
        
        img_2=np.zeros((img_1.shape[0:2]))
        img_2.shape
        img_3=np.zeros((img_1.shape[0:2]))
        img_3.shape
        img_4=np.zeros((img_1.shape[0:2]))
        img_4.shape
        
        
        threshold=200
        for i in range(img_1.shape[0]):
             for j in range(img_1.shape[1]):              
                n=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3 #gray level yapma
                img_2[i,j]=n
                if n>threshold: # BW yapma
                    img_3[i,j]=255 
                else: 
                    img_3[i,j]=0
            
        #plt.subplot(1,3,1),plt.imshow(img_1)
        #plt.subplot(1,3,2),plt.imshow(img_2,plt.cm.gray) 
        #plt.subplot(1,3,3),plt.imshow(img_3,plt.cm.binary)
        #plt.imshow(img_3,plt.cm.binary)
        
        for k in range(img_3.shape[0]):
            for t in range(img_3.shape[1]):
                img_4[k,t]=img_4[k,t]+img_3[k,t]/5
        
    center=img_4
    print(center)
    return center
centerA=resimleri_BW_yapma_center_bulma(lista)
centerB=resimleri_BW_yapma_center_bulma(listb)
centerC=resimleri_BW_yapma_center_bulma(listc)
centerD=resimleri_BW_yapma_center_bulma(listd)

#centerA ,centerB ,centerC ,centerD 

centerA.ndim, centerA.shape
centerB[0,0:30]
def distance(A,B):
    c=A-B
    d=c.sum()
    
    return d
d.sum()
