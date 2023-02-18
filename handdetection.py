import cv2
#import face_recognition
import time
import mediapipe as mp



global temptop, tempright, tempinit
temptop = 0
tempright = 0
tempinit = False

#def detectMovement(top, right):
#    if (top < temptop - 30 or top > temptop + 30 or right < tempright - 30 or right > tempright + 30):
#        print("Face detected!")


#face_locations = []
video = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    #time.sleep(1)

    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 20 :
                    cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    if (tempinit is False):
                        temptop = cy
                        tempright = cx
                        tempinit = True
                    elif(tempinit is True and (cy < temptop - 100 or cy > temptop + 100 or cx < tempright - 100 or cx > tempright + 100)):
                        print("Movement detected")

                        temptop = cy
                        tempright = cx

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

"""
    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(frameRGB)
    # Display the results

    for top, right, bottom, left in face_locations:
        if (tempinit is False):
            temptop = top
            tempright = right
            tempinit = True
        elif(tempinit is True and (top < temptop - 60 or top > temptop + 60 or right < tempright - 60 or right > tempright + 60)):
            print("Movement detected")
            temptop = top
            tempright = right


        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        tempinit = True
        """



