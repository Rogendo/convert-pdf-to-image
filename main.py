# Importing the pdf2image module
import re
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
import cv2

# convertin the pdf to img
image=convert_from_path('ImageProcessingTask.pdf')
for i in range(len(image)):
    image[i].save( "page" +str(i) +'.jpg','JPEG')


