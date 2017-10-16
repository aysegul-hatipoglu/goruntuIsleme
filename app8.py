import matplotlib.pyplot as plt
img_1=plt.imread("var.jpg")
img_2=plt.imread("yok.jpg")

plt.imshow(img_2-img_1)
plt.show()
