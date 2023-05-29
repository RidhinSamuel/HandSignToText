import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os
import shutil

try:
    data_name=input(" Enter the data name ")
    data_name=data_name.upper()
    path="D:\RIDHIN\COmputer\HandSignDetection\Data"
    folder=os.path.join(path,data_name)
    #folder=f"../Data/{data_name}"
    print("Folder name is",folder)
    if (os.path.exists(folder)==False):
        print(f"Data  is new creating folder {data_name}")
        os.mkdir(folder)
    else:
        ch=input("Do you want to overwrite the existing data ")
        if ch in "Yy":
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
except FileNotFoundError:
    print("File doesn exist")
cap = cv2.VideoCapture(0)
cap. set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap. set(cv2.CAP_PROP_FRAME_HEIGHT, 560)

detector = HandDetector(maxHands=1)

offset = 25
imgSize = 300

counter = 0

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key ==ord("q"):
        exit(1)
    if key == ord("s") :
        print("Taking short")
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter,"data collected");
        counter+=1
