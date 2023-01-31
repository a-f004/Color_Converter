# beforeImages内のすべてのファイルに対して処理を行う
# 処理が終わったファイルはafterImagesフォルダ内に連番で保存される
import cv2
import glob


i = 0
images = glob.glob("beforeImages/*")
for img in images:
    print(i)
    img = cv2.imread(img)
    height, width, channel = img.shape
    # print("height:", height)
    # print("width:", width)


    for x in range(height):
        for y in range(width):
            b, g, r = img[x, y]
            if (b, g, r) == (0, 0, 170):
                img[x, y] = 255, 255, 255
            else:
                img[x, y] = 0, 0, 0
    
    
    cv2.imwrite("afterImages/img_" + str(i) + ".png", img)
           
    i += 1

