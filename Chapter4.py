import cv2
import numpy as np

# # zero corresponds to black hence below code will create a black image
# img = np.zeros((512, 512))
# print(img.shape)    # shows that the image is a grayscale image

# makes an RGB image    BGR format n OpenCV
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# # coloring the image
# img[:] = 255, 0, 0  # colors the whole image blue
#
# # coloring a range of image
# img[100:250, 150:250] = 0, 0, 255   # colors a rectangle portion red

# creating lines
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 1)

# creating rectangles
cv2.rectangle(img, (10, 10), (502, 502), (0, 255, 0), 1)
cv2.rectangle(img, (100, 100), (412, 412), (0, 255, 0), cv2.FILLED)   # fills the area enclosed by the rectangle

# creating circles
cv2.circle(img, (256, 256), 150, (255, 0, 0), 3)

# putting text on images
cv2.putText(img, " OPEN CV ", (170, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 , 0, 0), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)