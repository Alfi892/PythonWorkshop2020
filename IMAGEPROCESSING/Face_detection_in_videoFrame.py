import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


video = cv2.VideoCapture(r"faceDetection.mp4")
#check, frame = video.read()
"""print(type(video))
print(type(check))
print(frame)
"""
check = True
while True:
    check, frame = video.read()

#cv2.destroyAllWindows()
    # img = cv2.imread("faceDetection.mp4")
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray_img,
    scaleFactor=1.3,
    minNeighbors=5)

    for x,y,w,h in faces:
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    # print(type(faces))
    # print(faces)

    # resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

    cv2.imshow("Gray",frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
video.release()
