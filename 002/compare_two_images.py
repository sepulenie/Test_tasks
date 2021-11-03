from os import path
from PIL import Image, ImageDraw
img_1 = Image.open('/home/maxim/python/Test_tasks/002/testimg_01.png')
img_2 = Image.open('/home/maxim/python/Test_tasks/002/testimg_02.png')

def checkpixels(img1 = Image, img2 = Image):
    pixels_list = [] 
    print(img1.size, img2.size)
    w = img1.width
    h = img1.height
    for i in range(h):
        for n in range(w):
            pixel1 = img1.getpixel((n,i))
            pixel2 = img2.getpixel((n,i))
            if pixel1 != pixel2:
                if abs(pixel1[0]-pixel2[0]) >= 20 or abs(pixel1[1]-pixel2[1]) >= 20 or abs(pixel1[2]-pixel2[2]) >= 20:
                    print(f'there is a wrong pixel, first one is {pixel1}, second is {pixel2}', abs(pixel1[0]-pixel2[0]))
                    pixels_list.append((n,i))
if img_1.size == img_2.size:
    img_3 = img_2
    img_3.save('/home/maxim/python/Test_tasks/002/testimg_03.png')
    checkpixels(img_1, img_2)
    

'''draw = ImageDraw.Draw(image)
draw.ellipse((140, 140, 340, 340), fill = False, outline ='red')
'''