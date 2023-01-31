# テスト用(1枚の画像)
import cv2

img = cv2.imread("beforeImages/test.png")
height, width, channel = img.shape
print("height:", height)
print("width:", width)


for x in range(height):
    for y in range(width):
        b, g, r = img[x, y]
        if (b, g, r) == (0, 0, 170):
            img[x, y] = 255, 255, 255
        else:
            img[x, y] = 0, 0, 0
    

cv2.imwrite("test.png", img)
           
    
  
