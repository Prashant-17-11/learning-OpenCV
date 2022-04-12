import cv2

# openCV convention for dimensions
# x-dimension is same as used in mathematics
# y-dimension is opposite to that used in mathematics
# for an image the origin is at the top-left most corner and the largest width and height at lower-right most corner

img = cv2.imread("Resources/feather.jpg")
print(img.shape)    # method to find the size of the image  (height, width, color_scales)

imgResize = cv2.resize(img, (300, 200))   # (width, height)
print(imgResize.shape)

imgResizeGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
print(imgResizeGray.shape)  # gray image only has one color scale (gray) so there would be no third value in output

imageCropped = img[0:200,50:150]    # [height, width]
print(imageCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Resize Gray", imgResizeGray)
cv2.imshow("Image Cropped", imageCropped)

cv2.waitKey(0)