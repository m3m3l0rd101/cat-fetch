from PIL import Image ,ImageFilter, ImageEnhance
import os


def add_files():
    folder = 'pics'
    files = [os.path.join(folder, f) for f in os.listdir(folder)]
    f = open('all_img.txt', 'w+') 
    f.read()
    for file in files:
        if f != file:
            f.write(file)
            f.write("\n")
        




def clean_up():
    add_files()
    f= open('all_img.txt', 'r+') 
    f.read()
    for file in f :
        img = Image.open(str(file))
        img = img.filter(ImageFilter.MedianFilter(size=3))
        img = img.resize((100, 80), Image.LANCZOS) 
        img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=3))
        img = ImageEnhance.Contrast(img).enhance(1.3)  
        

clean_up()

