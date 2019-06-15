"""
Developed and coded by:

Ali Zahid Raja

6/16/2019
"""


import cv2
import imageio
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
from tkinter import *
from tkinter import filedialog

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def dodge(front,back):
    for x in back:
        i = 0
        while i < len(x):
            #print(x[i])
            if x[i]==255:
                x[i]=254
            i+=1
    result=front*255/(255-back)
    result[result>255]=255

    return result.astype('uint8')


def convert():
    filename = filedialog.askopenfilename()
    # print(filename)

    img = filename
    start_img = imageio.imread(img)

    gray_img = grayscale(start_img)

    inverted_img = 255 - gray_img

    blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img, sigma=6)

    final_img = dodge(blur_img, gray_img)

    plt.imshow(final_img, cmap="gray")
    new_img = img[:-4] + '_new' + img[-4:]
    print(new_img)
    plt.imsave(new_img, final_img, cmap='gray', vmin=0, vmax=255)

    m = cv2.imread(new_img)

    cv2.imshow(new_img, m)

def main():
    master = Tk()

    button = Button(master, text="Convert", command=convert).pack()

    master.mainloop()


main()



