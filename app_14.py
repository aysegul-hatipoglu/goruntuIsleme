#iç kenar
#  2 lik matrisler
internal_mask_1=[[1,0],[0,0]]
internal_mask_2=[[0,1],[0,0]]
internal_mask_3=[[0,0],[1,0]]
internal_mask_4=[[0,0],[0,1]]
#dış kenar
external_mask_1=[[0,1],[1,1]]
external_mask_2=[[1,0],[1,1]]
external_mask_3=[[1,1],[0,1]]
external_mask_4=[[1,1],[1,0]]
import numpy as np
import matplotlib.pyplot as plt
size=3

img_1=np.random.randint(0,2,(size,size))
img_1  #fake image, you should read from a file
img_1=plt.imread('t.jpg')
img_1.ndim
img_1.shape
#plt.imshow(img_1,cmap='Greys',interpolation='nearest')
plt.imshow(img_1)
plt.show()

img_2=np.zeros((img_1.shape[0:2]))
img_2.shape
img_3=np.zeros((img_1.shape[0:2]))
img_3.shape

        
threshold=200
for i in range(img_1.shape[0]):
     for j in range(img_1.shape[1]):              
        n=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3 #gray level yapma
        img_2[i,j]=n
        if n>threshold: # BW yapma
            img_3[i,j]=255 
        else: 
            img_3[i,j]=0
            
plt.imshow(img_3,plt.cm.binary)
        
plt.show()
#m n li resimde 2,2 = mask lik matris arayacağım
def count_mask(image,mask):
    # input :
    # image m*n bw image
    # mask 2*2 mask
    
    counter=0
    m,n=image.shape
    for i in range(m-1):
        for j in range(n-1):
            a=b=c=d=False
            # 4 adet karşılaştırma sonrası hepsi true veririse counter ı 1 attıracağız
            if(image[i,j]== mask[0][0]):
                a=True
            if (image[i,j+1]==mask[0][1]):
                b=True
            if (image[i+1,j]==mask[1][0]):
                c=True
            if (image[i+1,j+1]==mask[1][1]):
                d=True
            
            if(a and b and c and d):
                counter=counter+1
                
    return counter
    #iç kenar
#  2 lik matrisler
i_mask_1=[[1,0],[0,0]]
i_mask_2=[[0,1],[0,0]]
i_mask_3=[[0,0],[1,0]]
i_mask_4=[[0,0],[0,1]]
e_mask_1=[[0,1],[1,1]]
e_mask_2=[[1,0],[1,1]]
e_mask_3=[[1,1],[0,1]]
e_mask_4=[[1,1],[1,0]]
i_m_l=[i_mask_1,i_mask_2,i_mask_3,i_mask_4]
e_m_l=[e_mask_1,e_mask_2,e_mask_3,e_mask_4]
def counter_internal_mask(image):
    counter_internal=0
    for mask in i_m_l:
        counter_internal=counter_internal+count_mask(img_3,mask)
    return counter_internal
def counter_external_mask(image):
    counter_external=0
    for mask in i_m_l:
        counter_external=counter_external+count_mask(img_3,mask)
    return counter_external
c_1=counter_internal_mask(img_3)
c_2=counter_external_mask(img_3)
c_1,c_2
img_3.ndim
