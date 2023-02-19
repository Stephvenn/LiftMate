import cv2

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

awake = False
count = 0
while not awake:

    ret, frame = video.read()
    #frame = cv2.flip(frame, 1)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(frameGray,1.3,5)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        count += 1
        #function call


    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()



