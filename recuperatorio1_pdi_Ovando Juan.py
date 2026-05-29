#Recuperatorio Parcial 1 - Proc. de Imágenes - Ovando Juan. 

import streamlit as st
import cv2
import numpy as np
from PIL import Image

#Configuración página
st.set_page_config(page_title="Escáner de facturas inteligente", layout="wide")

st.title("Escáner de documentos con OpenCV")
st.write("Sube una foto para procesarla")