from io import BytesIO
from PIL import Image
import sys

path_to_image = input("input the img/jpg file path:")
x, y = 40, 40
im = Image.open(path_to_image).convert('1')
im_resize = im.resize((x,y))
buf = BytesIO()
im_resize.save(buf, 'ppm')
byte_im = buf.getvalue()
temp = len(str(x) + ' ' + str(y)) + 4
print(byte_im[temp::])

