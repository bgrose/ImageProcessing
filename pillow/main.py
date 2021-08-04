from PIL import Image

im = Image.open("lena.py")
im.show()
im = im.rotate(45)
im.show()
