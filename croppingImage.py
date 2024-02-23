import cv2



# soo aqri sawirka..
img = cv2.imread('3balls.png')



# formula: y1:y2, x1,x2
# (x=7, y=80)
# (x=117, y=199)
redBall = img[80:199, 7:117]


# new image sameeey, sawirkii hore oo fulllka ka ahaa kasoo qaad oqeebtii aan doorane.
cv2.imwrite('redball.png', redBall)


# soo bandhig full iamgeka.
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

