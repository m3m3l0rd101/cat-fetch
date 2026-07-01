from ascii_magic import AsciiArt
import random 
import sys
import os


def findf(path,files):
    files = next(os.walk(path))
files = ['/home/teto3-3/cat-fetch/pics/dumb.jpg']
findf('/home/teto3-3/cat-fetch/pics',files)
for f in files :
    print (f)