import cv2
image=cv2.imread('img.png')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Color Image',image)
cv2.imshow('Grayscale Image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import Image
img=Image.open('img.png')
gray_img=img.convert('L')
img.show(title="Original Image")
gray_img.show(title="Grayscale Image")
gray_img.save('output_gray.jpg')

from skimage import io, color
import matplotlib.pyplot as plt
original_image = io.imread('img.png')
height, width, channels = original_image.shape
print(f"Image loaded with height: {height}, width: {width}, and channels")
gray_image=color.rgb2gray(original_image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title("Actual Color Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title("Greyscale Image")
plt.axis('off')
plt.show()
