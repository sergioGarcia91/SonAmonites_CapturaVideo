# Detección de Amonites con OpenCV y YOLOv8

Este repositorio contiene un script en Python para visualizar los resultados de la detección de amonites utilizando un modelo CNN obtenido del Notebook [07a_YOLOv8_Amonites_20240323](https://github.com/sergioGarcia91/ML_and_EDA/blob/4081aacb63afe9fe88db9c1beeb047cb519f9813/07a_YOLOv8_Amonites_20240323.ipynb).

El modelo se basa en YOLOv8 y se ha reentrenado específicamente para detectar amonites. Puedes encontrar información detallada y tutoriales sobre YOLOv8 en su [documentación oficial](https://docs.ultralytics.com/es).

Para el entrenamiento, se utilizaron 80 imágenes y 20 imágenes para la validación. Se recomienda aumentar la cantidad de imágenes para mejorar la generalización del modelo. Además, se utilizaron herramientas como [Roboflow](https://roboflow.com) para la preparación de los datos.

En el repositorio se encuentran disponibles tres archivos `.pt`, que pueden modificarse en el script para evaluar diferentes resultados:

- **SonAmonites_v1.pt:** Modelo obtenido del CNN sin aumento de datos.
- **SonAmonites_v2.pt:** Modelo obtenido del CNN con aumento de datos.
- **yolov8n.pt:** Modelo original de YOLOv8, que cuenta con muchas más categorías en la detección.

<p align="center">
  <img src="https://github.com/sergioGarcia91/SonAmonites_CapturaVideo/blob/fcab1a3586548ac179772fd8eb8ad4e7b1a91e1e/navegador_resize.gif" alt="Amonites">
</p>

