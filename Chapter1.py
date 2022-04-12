import cv2
# cv2 stands for computer vision

print("Package Imported!")

# # reading images
# img = cv2.imread("Resources/feather.jpg")
#
# # displaying images, the wait key is added to keep the frame visible
# cv2.imshow("Output",img)
# cv2.waitKey(0)


# # Reading video
# cap = cv2.VideoCapture("path")
#
# # Displaying video
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break



# Reading video from webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(10,50)    # to adjust brightness settings

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
