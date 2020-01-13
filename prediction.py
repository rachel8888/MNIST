import tensorflow as tf
import numpy as np
def load_model():
    new_model = tf.keras.models.load_model('epic_num_reader.model')
    return new_model

from PIL import Image , ImageFilter

def imageprepare(argv):
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L',(28,28), (255))
    
    if width> height:
        nheight = int(round((20.0 / width * height), 0))
        if (nheight == 0):
            nheight = 1
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        vtop = int(round(((28 - nheight) / 2), 0))
        newImage.paste(img , (4, vtop))
    else:
        nwidth = int(round((20.0/ height * width), 0))
        if (nwidth == 0):
            nwidth = 1
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))
        newImage.paste(img , (wleft, 4))
    tv = list(newImage.getdata())
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva
x = [imageprepare('epic_num_reader.model\Images\madeone.png')]

newArr= [[0 for d in range(28)] for y in range(28)]
k = 0 
for i in range(28):
    for j in range(28):
        newArr[i] [j] = x[0] [k]
        k = k + 1

t = []
t.append(newArr)
t = np.asarray(t)
t.shape
load_model()
predictions = load_model().predict(t)

print("Predicted digit is:", end = '')
print(np.argmax(predictions[0]))
