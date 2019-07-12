print("Performing OCR...\n")

try:
    from PIL import Image
except ImportError:
    import Image
from pytesseract import Output
import pytesseract as pyt
from googletrans import Translator
import cv2

#This is performing the OCR
pyt.pytesseract.tesseract_cmd=r'/usr/bin/tesseract'
word = (pyt.image_to_string( Image.open('test.jpg') ) )
print "Original Text"
print word

#This is performing the translation
translator = Translator()
translation = translator.translate(word, dest='fr') #to change the language, insert langauge code inside the '__'
print "\nText translated to French"
print translation.text

#This places a bounding box on the image that OCR was performed on
d = pyt.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d)
for i in range(n_boxes):
	(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i] )
	cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
