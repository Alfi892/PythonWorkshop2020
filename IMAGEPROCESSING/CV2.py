import cv2
li=["ml.jpeg","im2.jpeg","im3.jpeg","im4.jpeg","im5.jpeg","im6.jpeg","im7.jpeg","im8.jpeg","im9.jpg","im.jpg",1]

#print(img)
"""print(type(img))
print(img.shape)
print(img.ndim)"""
#cv2.imshow("ml",img)
#cv2.waitKey(9000)
#cv2.destroyAllWindows

"""resize_img = cv2.resize(img,(40,70))
cv2.imshow("newIMG",resize_img)
cv2.waitKey(2000)"""


for i in li:
    i=cv2.imread(i,1)
    r_img = cv2.resize(i,(int(i.shape[0]/2),int(i.shape[1]/2)))
    cv2.imshow("newim",r_img)
    cv2.waitKey(2000)
    cv2.imwrite("newim_rsr.jpeg",r_img)

