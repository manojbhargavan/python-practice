import cv2 as cv
import numpy as np


def av_pix(img, circles_np, size):
    av_values = []
    for coordinates in circles_np[0, :]:
        col = np.mean(img[coordinates[1] - size:coordinates[1] + size, coordinates[0] - size:coordinates[0] + size])
        av_values.append(col)
    return av_values


def get_radius(circles_np):
    radius = []
    circle_count = 1
    for circle in circles_np[0, :]:
        radius.append(circle[2])
        circle_count += 1

    return radius


coin_image = cv.imread("resources/19.2 capstone_coins.png")
coin_image_gray = cv.imread("resources/19.2 capstone_coins.png", cv.IMREAD_GRAYSCALE)
coin_image_blur = cv.GaussianBlur(coin_image_gray, (5, 5), 0)

# cv.imshow("Coins", coin_image)
# cv.imshow("Coins Blur", coin_image_blur)
# cv.imshow("Coins Gray", coin_image_gray)

# Hough Circle
cimg = cv.cvtColor(coin_image_blur, cv.COLOR_GRAY2BGR)
coin_circle = cv.HoughCircles(coin_image_blur, cv.HOUGH_GRADIENT, 0.9, 120, param1=50, param2=27, minRadius=60,
                              maxRadius=120)
circles = np.uint16(np.around(coin_circle))
count = 1
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(coin_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(coin_image, (i[0], i[1]), 2, (0, 0, 255), 3)
    count += 1

radii = get_radius(circles)
print(radii)

bright_values = av_pix(coin_image_gray, circles, 20)
print(bright_values)

values = []
for a, b in zip(bright_values, radii):
    if a > 150 and b > 110:
        values.append(10)
    elif a > 150 and b <= 110:
        values.append(5)
    elif a < 150 and b > 110:
        values.append(2)
    elif a < 150 and b < 110:
        values.append(1)
print(values)

count_2 = 0
for i in circles[0,:]:
    cv.putText(coin_image, str(values[count_2]) + 'p', (i[0], i[1]), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)
    count_2 += 1
cv.putText(coin_image, 'Estimated Total Value: ' + str(sum(values)) + 'p', (200, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

cv.imshow('detected circles', coin_image)
cv.waitKey(0)
cv.destroyAllWindows()
