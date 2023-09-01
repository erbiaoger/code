import numpy as np
import cv2 as cv
from ultralytics import YOLO
import numpy as np


model = YOLO("yolov8m.pt")

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    #print(frame.shape)
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 我们在框架上的操作到这里
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #frame = cv.cvtColor(frame, 1)
    results = model(frame)
    result = results[0]
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    classes = np.array(result.boxes.cls.cpu(), dtype="int")
    #print(bboxes.shape, classes)
    (x, y, x2, y2) = bboxes[0]

    cv.rectangle(frame, (x, y), (x2, y2), (0, 0, 225), 2)
    cv.putText(frame, str(classes), (x, y - 5), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 225), 2)

    # 显示结果帧e
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release()
cv.destroyAllWindows()

