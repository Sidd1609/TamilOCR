import tensorflow as tf
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import sys
##X,Y = pickle.load(open('tam.pickle','rb'))
##X=X.reshape(-1,100,100,1)
##Y=np.array(Y).reshape(-1,1)
d=['\u0B95','\u0B99','\u0B9A','\u0B9E','\u0B9F','\u0BA3','\u0BA4','\u0BA8',
   '\u0BAA','\u0BAE','\u0BAF','\u0BB0','\u0BB2','\u0BB5','\u0BB4','\u0BB3','\u0BB1','\u0BA9']
model=load_model('fin.h5')
ar='im0.jpg'
x=cv2.imread(ar)
x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
x=cv2.resize(x,(100,100))
(thresh, x) = cv2.threshold(x, 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
x=x/255
x=x.astype('uint8')
x=np.array(x).reshape(1,100,100,1)
p=model.predict([x])
p=np.ndarray.tolist(p.reshape(-1,1))
#print(p)
i=p.index(max(p))
print(d[i])
##model.evaluate(X,Y)
