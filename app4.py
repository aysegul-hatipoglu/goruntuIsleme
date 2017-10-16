a=10
print(a)
import math
def findDistance(x,y):
    return math.sqrt(
    (x[0]-y[0])**2
    +
    (x[1]-y[1])**2)
d=findDistance([3,0],[0,4])
d
from scipy import ndimage
from scipy import misc
f=misc.face()
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
f.ndim
type(f)
f[:,:,2]=0.0
plt.imshow(f)
plt.show()
f.shape
type(f.shape)
im_size=f.shape
im_size[0]
center=[im_size[0]/2,im_size[1]/2]
for i in range(im_size[0]):
    for j in range(im_size[1]):
        if (findDistance([i,j],center)>100):
            f[i,j,:]=0
plt.imshow(f)
plt.show()
