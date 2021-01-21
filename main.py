import cv2
import numpy as np
import imutils
from pyzbar import pyzbar

video = cv2.VideoCapture(0) #'http://192.168.0.100:4747/video'

while True:
    is_ok, frame = video.read()

    if is_ok:
        frame = imutils.resize(frame, 400)

        qrcodes = pyzbar.decode(frame)

        for qrcode in qrcodes:
            (x, y, w, h) = qrcode.rect
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)

            qrcodedata = qrcode.data.decode("utf-8")
            qrcodetype = qrcode.type

            text = f"{qrcodedata}"

            print(qrcodedata)

            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow("Registro de Ponto", frame) 
        k = cv2.waitKey(30) & 0xff #pega a tecla esc
        if k == 27: #caso esc for apertado para
            break

    else:
        print("erro ao iniciar captura!")
        break;