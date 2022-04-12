import cv2
import numpy as np

img = cv2.imread("Resources/feather.jpg")

cv2.imshow("Image", img)
# cv2.waitKey(0)

# cvtColor is used to alter the color specifications of an image
# first parameter is the image
# second is cv2.COLOR method used to define the conversion
# cv2 uses BGR instead of standard RGB
# COLOR_BGR2GRAY method is used to convert a colored image to GrayScale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", imgGray)
# cv2.waitKey(0)

# GaussianBlur method is used to blur images
# first parameter defines the image source
# second parameter ksize defines the kernel size    - it has to be odd
# third parameter is sigmaX
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

cv2.imshow("Blur Image", imgBlur)
# cv2.waitKey(0)

# edge detector in image
# the higher the threshold values less the number of edges
# imgCanny = cv2.Canny(img, 100, 100)
imgCanny = cv2.Canny(img, 200, 200)

cv2.imshow("Canny Image", imgCanny)
# cv2.waitKey(0)

# image Dilation
# increasing the edge thickness
# changing the kernel size affects the thickness
kernel = np.ones((3, 3), np.uint8)  # requires numpy module
# changing the iterations also affects the thickness
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("Dilated image", imgDilation)
# cv2.waitKey(0)

# image Erosion
# reducing the edge thickness
imgEroded = cv2.erode(imgDilation, kernel)

cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)