import numpy as np
import cv2
renkli_resim=cv2.imread('orjinal.jpg',cv2.IMREAD_COLOR)
gri_resim=cv2.imread('orjinal.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('renkli_resim',renkli_resim)
cv2.imshow('gri_resim',gri_resim)
cv2.imwrite('renkli.jpg',renkli_resim)
cv2.imwrite('gri.jpg',gri_resim)
from matplotlib import pyplot as plt
img = cv2.imread('orjinal.jpg',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
