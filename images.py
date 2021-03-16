from PIL import Image, ImageFilter

img = Image.open('./images/astro.jpg')
img.thumbnail((400, 400))
print(img.size)
img.save('./images/thumbnail.jpg')

