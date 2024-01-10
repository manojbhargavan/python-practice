import cv2

img = cv2.imread("resources/lena.png")
cv2.imshow("Original", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", img_gray)

img_blur = cv2.GaussianBlur(img, (17, 7), 0)
cv2.imshow("Blur Image", img_blur)

img_canny = cv2.Canny(img, 50, 55)
cv2.imshow("Canny Image", img_canny)

cv2.waitKey(5000)
cv2.destroyAllWindows()
