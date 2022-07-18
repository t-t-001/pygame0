from PIL import Image

img = Image.open('./images/spaceRockets_001.png')
img_resize = img.resize((50,100))
img_resize.save('./images/rocket.png')