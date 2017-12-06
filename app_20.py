import matplotlib.pyplot as plt
import numpy as np
def convert_RGB_to_monochrome_BW(image_1,threshold=100):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if(img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,1]/3)>threshold:
                img_2[i,j]=0
            else:
                img_2[i,j]=1
    return img_2

def define_mask_1():
    mask_1=[[1,1,1],[1,1,1],[1,1,1]]
    #mask,mask[1][2],mask[0][0],mask[2][2] #mask[3][1] error
    for i in range (3):
        for j in range(3):
            print(mask_1[i][j],end=" ")
        print()
    return mask_1

def my_dilation(img_1,mask):
    m=img_1.shape[0]
    n=img_1.shape[1]
    img_2=np.random.randint(0,1,(m,n))
    for i in range (1,m-1):
        for j in range(1,n-1):
            x_1=img_1[i,j] and mask[1][1]
            x_2=img_1[i-1,j-1] and mask[0][0]
            x_3=img_1[i-1,j] and mask[0][1]
            x_4=img_1[i-1,j+1] and mask[0][2]
            x_5=img_1[i+1,j-1] and mask[2][0]
            
            x_6=img_1[i+1,j] and mask[2][1]
            x_7=img_1[i+1,j+1] and mask[2][2]
            x_8=img_1[i,j-1] and mask[1][0]
            x_9=img_1[i,j+1] and mask[1][2]
           
 result_1=x_1 or x_2 or x_3 or x_4 or x_5
            result_2=x_6 or x_7 or x_8 or x_9 
            result= result_1 or result_2
            img_2[i,j]=result         
    return img_2
mask=define_mask_1()
path_file=u"c:\\Users\\aysegul\latter.jpg"
i_100=convert_RGB_to_monochrome_BW(path_file)
i_200=my_dilation(i_100,define_mask_1())
plt.subplot(1,2,1),plt.imshow(i_100,plt.cm.gray)
plt.subplot(1,2,2),plt.imshow(i_200,plt.cm.gray)
plt.show()

i_200=my_dilation(i_200,define_mask_1())
plt.subplot(1,2,1),plt.imshow(i_100,plt.cm.gray)
plt.subplot(1,2,2),plt.imshow(i_200,plt.cm.gray)
plt.show()


