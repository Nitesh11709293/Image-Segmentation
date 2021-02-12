#import cv2
#img=cv2.imread("‪C:\Users\Nitesh Singh\Downloads\panda'.jpg")
#cv2.imshow("img",img)
#cv2.waitkey(1000)
import cv2
 
image = cv2.imread(r"C:\\Users\Nitesh Singh\Downloads\panda.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
