import matplotlib.pyplot as plt
import numpy as np
pwd
ls *.jpg
img_1=plt.imread("test_1.jpg")
img_1.ndim
img_1.shape
img_2=img_1[1:768:2,1:1024:2]
img_2.ndim,img_2.shape
plt.imshow(img_2)
plt.show()
img_2
img_4=np.zeros((img_2.shape[0:2]))
img_4.shape
threshold=80
for i in range(img_2.shape[0]):
    for j in range(img_2.shape[1]):
        n=img_2[i,j,0]/3+img_2[i,j,1]/3+img_2[i,j,2]/3
        img_3[i,j]=n
        if n>100:#esik deger
            img_4[i,j]=255
        else:
            img_4[i,j]=0
plt.subplot(1,3,1),plt.imshow(img_2)
plt.subplot(1,3,2),plt.imshow(img_3,plt.cm.gray)
plt.subplot(1,3,3),plt.imshow(img_4,plt.cm.binary)
img_3.shape
plt.imshow(img_4,plt.cm.gray)
plt.show()
plt.imshow(img_3,plt.cm.gray)
plt.show()
img_4=np.zeros((img_2.shape[0:2]))
img_4.shape
