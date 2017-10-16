import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#degisken img(min,max)
#inverce alacagiz
img=mpimg.imread(r'C:\Users\MUTLU\goruntuIsleme\stinkbug.png')
img.ndim
img.shape
plt.imshow(img)
plt.show()#yüzde 50 kırpılmış halidir
img[:,100,:].max()#1.kolondaki butun renlerin max i
img_1=img[1:375:2,:,:]#butun rgb yi al 2 ser artarak
img_1=img[:,1:500:2,:]
plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(img_1)
#plt.imshow(img_1)
plt.show()
img.ndim,img.shape
img_20=np.zeros((500,375,3))# boyutlarında img_20 adında matris oluşturur. Matris boyutları transpozesinde simetrik olacak
img_20.shape
for i in range(375):
    for j in range(500):
        img_20[j,i,:]=img[i,j,:]
plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(img_20)
#plt.imshow(img_1)
plt.show()
img_30=np.zeros((500,375,3))
img_30.shape
for i in range(375):
    for j in range(500):
        img_30[j,i,:]=1-img[i,j,:]#img isimli 3 boyutlu kubun transpozu
        #img[i,j,:]

img_40=np.zeros((375,500,3))
img_40.shape
for i in range(375):
    for j in range(500):
        img_40[375-i-1,500-j-1,:]=1-img[i,j,:]
img_50=np.zeros((375,500,3))
img_50.shape
for i in range(375):
    for j in range(500):
        img_50[375-i-1,j,:]=1-img[i,j,:]
plt.subplot(2,3,1),plt.imshow(img)
plt.subplot(2,3,2),plt.imshow(img_20)
plt.subplot(2,3,3),plt.imshow(img_30)
plt.subplot(2,3,4),plt.imshow(img_30)
plt.subplot(2,3,5),plt.imshow(img_40)
plt.subplot(2,3,5),plt.imshow(img_50)
plt.show()
