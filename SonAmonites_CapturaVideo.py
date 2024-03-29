# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:21:14 2024

@author: Sergio Andrés García Arias

Video de referencia:
    SEGMENTACIÓN DE INSTANCIAS Y DETECCIÓN DE OBJETOS PERSONALIZADA | Entrenamiento paso a paso YoloV8
    https://www.youtube.com/watch?v=rk7zOBRJWCc
"""

# Importar librerias
from ultralytics import YOLO
import cv2

# Leer el modelo a utilizar
model = YOLO('SonAmonites_v1.pt')
#model = YOLO('SonAmonites_v2.pt')
#model = YOLO('yolov8n.pt') # probar la de YOLOv8

# Capturar la imagen de la camara
capCamara = cv2.VideoCapture(0)

# Bucle
while True:
    # Leer los fotogramas
    ret, frame = capCamara.read()
    
    # Predecir resultado
    resultadosCNN = model.predict(frame, imgsz=640, conf=0.35)
    
    # Mostrar resultados
    resultadoFrame = resultadosCNN[0].plot()
    
    # Mostrar captura
    #cv2.imshow('Son Amonites', frame) # la camara sola
    cv2.imshow('Son Amonites', resultadoFrame) # los resultados de la prediccion
    
    # Cerrar la ventana al pulsar la tecla Esc
    if cv2.waitKey(1) == 27: 
        break

capCamara.release()
cv2.destroyAllWindows()