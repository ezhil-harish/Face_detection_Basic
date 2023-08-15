import cv2
train = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
while True:
    success, frame = video.read()
    if success==True:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = train.detectMultiScale(image)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.imshow('video', frame)
        key = cv2.waitKey(1)
        if key == 45:
            print("hii")
            break
    else:
        print("over")
