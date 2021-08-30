import pytesseract as tess
from deep_translator import GoogleTranslator
import cv2
tess.pytesseract.tesseract_cmd = r'C:\Users\Sachit Ramesh Gowda\Desktop\tess\tesseract.exe'
from PIL import Image

img_cv = cv2.imread('text.png')
text = tess.image_to_string(img_cv)
tar=input("Target Language")
print(text)
translated = GoogleTranslator(source='auto', target=tar).translate(text)
print(translated)


