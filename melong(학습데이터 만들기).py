from PIL import Image
import PIL.Image as pilimg
import random
import numpy as np

filepath='./indigestion/'

for i in range(1, 11):
    img = Image.open(filepath +"indigestion (%s).jpg" % i)
    img2 = Image.open(filepath + "indigestion (%s).jpg" % i)
    resize = img.resize((512, 512))
    resize2 = img2.resize((512, 512))

    print(resize.size)
    print(resize.format)

    #img.show()

    def dark(x):
        global a
        return x-a

    def white(y):
        global b
        return y+b

    for a in range(50):
        result_d = Image.eval(resize2, dark)  # lambda x : x-100)
        result_d.save("./result_indigestion/result_indigestion_d_%s_%s.jpg" % (i, a))

    for b in range(50):
        result_w = Image.eval(resize, white)#lambda x : x-100)
        result_w.save("./result_indigestion/result_indigestion_w_%s_%s.jpg" % (i, b))

