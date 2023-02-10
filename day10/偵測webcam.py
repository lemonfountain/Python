import cv2

# 人臉特徵黨
face_casade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")


# 設定 Webcam
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    ret, frame = cap.read()
    print(ret, frame)

# 釋放資源
cap.release()
cv2.destroyAllWindows()

