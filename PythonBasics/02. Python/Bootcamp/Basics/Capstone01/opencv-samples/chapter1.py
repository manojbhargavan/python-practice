import cv2

# Import Image and Show
img = cv2.imread("resources/lena.png")
cv2.imshow("Lena", img)
cv2.waitKey(0)


# Import Video
vd_cap = cv2.VideoCapture("resources/sample.mp4")
while True:
    success, img = vd_cap.read()
    cv2.imshow("Sample", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video Cam
vd_cam = cv2.VideoCapture(0)
vd_cam.set(3, 640)
vd_cam.set(4, 480)
while True:
    success, img = vd_cam.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
