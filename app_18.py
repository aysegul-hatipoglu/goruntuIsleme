import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.misc import imsave
%matplotlib inline

def convert_RGB_to_monochrome_BW(image_1,threshold=100):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if(img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,1]/3)>threshold:
                img_2[i,j]=1
            else:
                img_2[i,j]=0
    return img_2

image_file_1=r"test_t_one.jpg"
img_1=convert_RGB_to_monochrome_BW(image_file_1,threshold=100)
plt.imshow(img_1,cmap='gray')
plt.show()
img_1.ndim, img_1.shape
i2=img_1.reshape(1,img_1.shape[0]*img_1.shape[1])
i2.ndim, i2.shape
def get_Histogram(image): #image monochrome olmalı
    my_Histogram={}
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            item=image[i,j]
            if item in my_Histogram.keys():
                my_Histogram[item]=my_Histogram[item]+1
            else:
                my_Histogram[item]=1
                
                
    return my_Histogram

my_Histogram=get_Histogram(img_1)
my_Histogram
x=my_Histogram[0.0]
y=my_Histogram[1.0]
print("siyah beyaz oranı: ",x/y)
class myMatrix():
    def __init__(self,x,y):
        self.D=x
        self.F=y

def create_D_F(img_1):
    d={(i,j) for i in range(img_1.shape[0])
             for j in range(img_1.shape[1])
             if img_1[i,j]==1
      }
    f={(i,j):1 for i,j in d}
    
    m=myMatrix(d,f)
    return m

my_sparce_Matrix_1=create_D_F(img_1)
my_sparce_Matrix_1.D, my_sparce_Matrix_1.F
