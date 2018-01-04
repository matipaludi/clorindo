#!/usr7bin/env python

print "hello world"
from PIL import Image
print "hello world 2 "
from tesseract import *
print "3"

image_file = 'prueba1.jpg'
im = Image.open(image_file)
print "tomo imagen"
text = image_to_string(im)
text = image_to_string(image_file)
text = image_to_string(image_file,gracefull_errors=True)
print "terminado"
print text

