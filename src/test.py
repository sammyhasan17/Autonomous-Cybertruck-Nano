


import cv2 
# create a 200x200 black image directly with cv2
img = cv2.imread("/usr/share/rpd-wallpaper/road.jpg")  # sample Pi wallpaper

if img is None:
    print("cv2 loaded, but sample image not found")
else:
    cv2.imshow("CV2 Test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
