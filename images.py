from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
filtered_img.save('./images/pikachu_gray.png', 'png')
