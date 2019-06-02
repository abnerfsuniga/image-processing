from PIL import Image

im = Image.open('dog.jpg')
im2 = im.quantize(colors=32, method=0)
im2.show()
im2.save()