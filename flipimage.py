import cv2
image=cv2.imread('img.png')
flipped_image=cv2.flip(image,1)
cv2.imshow("Origianl Image",image)
cv2.imshow("Flipped Image",flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
