import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)

tipIds = [4,8,12,16,20]

def fingerPosition(image,handNo = 0):
    lmList = []
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]
        for id,lm in enumerate(myHand.landmark):
            print(id,lm)
            h,w,c = image.shape
            cx,cy = int(lm.x*w),int(lm.y*h)
            lmList.append([id,cx,cy])
        return lmList

while True:
    success, image = cap.read()

    #cv2.imshow("Media Controller", image)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image = cv2.flip(image,1)
    results = hands.process(image)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)

    fingerPosition(image)
    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

