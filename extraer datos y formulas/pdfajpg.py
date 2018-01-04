print 'hello world1'
#import imagemagick
#img = Magick.read('NIR.pdf')
#print 'hello world'
#convert -density 600 NIR.pdf NIR.jpg

#~/Escritorio/clorindo appo$ convert NIR.pdf NIRjpg
#~/Escritorio/clorindo appo$ ls
#NIR.pdf
#NIR-1.jpg
#NIR-2.j
import os
os.system("convert -density 600 NIR.pdf NIR.jpg")

