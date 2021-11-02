from PIL import Image
img_1 = Image.open('/home/maxim/python/Test_tasks/002/testimg_01.png')
img_2 = Image.open('/home/maxim/python/Test_tasks/002/testimg_02.png')

def checkpixels(img1 = Image, img2 = Image):
    print(img1.size, img2.size)
    w = img1.width
    h = img1.height
    for i in range(h):
        for n in range(w):
            print(getpixel(img1, n,i))
            





if img_1.size == img_2.size:
    checkpixels(img_1, img_2)
