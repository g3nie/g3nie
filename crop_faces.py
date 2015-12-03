# Code modified from Michael Guerzhoy of UofT 
# Thank you Michael for a great course

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import urllib

gg = ['taeyeon', 'jessica', 'tiffany', 'yuri', 'yoona', 'hyoyeon', 'seohyun', 'sunny', 'sooyoung']
# gg_dataset.txt
# gg_test.txt
# Our dataset ignores a few metadata, particularly numbering and checksum
# name - numbering - url - bounding box x1,y1,x2,y2

def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    '''From:
    http://code.activestate.com/recipes/473878-timeout-function-using-threading/'''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return False
    else:
        return it.result

testfile = urllib.URLopener()            

# Allowable extensions
extensions = ["jpeg", "jpg", "png","gif"]
for line in open("gg_dataset.txt"):
    # if line is empty: skip
    current = line.split()
    if current == []:
        continue

    # current[0] -> name
    # current[1] -> number
    # current[2] -> bounding box
    # current[3] -> url
    filename = current[0] + '_' + current[1] + '.png'
    x1, y1, x2, y2 = map(int, current[2].split(','))
    url = current[3]

    timeout(testfile.retrieve, (url, "data/" + filename), {}, 30)
    try:
        pic = imread("data/" + filename)
        picShape = pic.shape

        face = pic[y1:y2, x1:x2]
        #print "Pic shape after cropping the face " + str(face.shape)
        # resize, note: face.shape() -> (x,y,3)
        # plt.gray() 
        # Smooth resize
        while face.shape[0] > 64:
            face = imresize(face, .5)
        face = imresize(face, [32,32])

        # print "Resized shape " + str(resized.shape)
        imsave("data/" + filename, face)
    except Exception as e:
        print e
        continue
