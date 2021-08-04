from PIL import Image, ImageFilter


im = Image.open("black-organic-sesame-seeds-isolated-260nw-664802284.jpg")
im.show()
im.rotate(45).show()

print(str(im.info))

r, g, b = im.split()
im.show()
image = Image.merge("RGB", (b, g, r))
image.show()

blurImage = im.filter(ImageFilter.BLUR)
blurImage.show()
#Save blurImage
blurImage.save('simBlurImage.jpg')



#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
#Create image object
#Applying the blur filter
img1 = im.filter(CONTOUR)
img1.save('ImageFilter_blur.jpg')
img1.show()

