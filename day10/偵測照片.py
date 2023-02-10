# 偵測照片, 並將人臉, 眼睛, 微笑偵測出來
# 安裝: pillow, opencv-python, opencv-contrib-python
import cv2
# 人臉特徵檔
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
print(face_cascade)

# 讀取影像檔(原始圖，為彩色)
frame = cv2.imread("./sample_image/test.jpg")

# 讀取灰階影像;好處是分析快速
gray = cv2.cvtcolor(frame, cv2.COLOR_BGRGRAY)

# 顯示影像
cv2.imshow("My Image", gray)

# 按下任意鍵離開
c = cv2.waitKey(0)  # 0代表系統會等待輸入然後才反應run; 1 代表系統會自動先跑
print(c)
