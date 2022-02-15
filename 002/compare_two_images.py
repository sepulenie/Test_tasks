#Две почти одинаковые картинки, на третьей кружком обведены точки, которые во внешнем редакторе нарисовали на второй.

from os import path
from PIL import Image, ImageDraw
img_1 = Image.open('002/testimg_01.png')
img_2 = Image.open('002/testimg_02.png')

def checkpixels(img1 = Image, img2 = Image):
    pixels_list = []
    w = img1.width
    h = img1.height
    for i in range(h):
        for n in range(w):
            pixel1 = img1.getpixel((n,i))
            pixel2 = img2.getpixel((n,i))
            if pixel1 != pixel2:
                if abs(pixel1[0]-pixel2[0]) >= 20 or abs(pixel1[1]-pixel2[1]) >= 20 or abs(pixel1[2]-pixel2[2]) >= 20:  #цвета пикселей на одинаковых картинках могут быть немного разными
                    pixels_list.append((n,i))
    return pixels_list

def drawcircles (pixels_list = list):
    img_3 = img_2
    draw = ImageDraw.Draw(img_3, 'RGBA')
    for c in pixels_list:
        abswidth = abs(img_3.size[0]-c[0])
        absheigh = abs(img_3.size[1]-c[1])
        if  abswidth >= 20 and absheigh >= 20:
            draw.ellipse((c[0]-20, c[1]-20, c[0]+20, c[1]+20), fill= False, outline='red')
        else:
            r = min(absheigh, abswidth)
            draw.ellipse((c[0]-r, c[1]-r, c[0]+r, c[1]+r), fill= False, outline='red')
    img_3.save('002/testimg_03.png')


if img_1.size == img_2.size:
    b = checkpixels(img_1, img_2)
    drawcircles(b)