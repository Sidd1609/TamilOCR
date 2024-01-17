import cv2
import os
import tifffile as tiff
import matplotlib.pyplot as plt
import numpy as np
import sys
import random
np.set_printoptions(threshold=50)
for i in os.listdir('/content/tamil_dataset_offline'):
  for im in os.listdir(f'/content/tamil_dataset_offline/{i}'):
    if(im[0]=='0'):
      d=int(im[1])*10+int(im[2])
      if(d>=12 and d<=29):
        if(im[7]=='t'):
          x=tiff.imread(f'/content/tamil_dataset_offline/{i}/{im}')
          x=x.astype('uint8')
          x=cv2.resize(x,(100,100))         
        else:
          x=cv2.imread(f'/content/tamil_dataset_offline/{i}/{im}')
          x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
          x=cv2.resize(x,(100,100))
          (thresh, x) = cv2.threshold(x, 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
          x=x/255
          x=x.astype('uint8')
          # print(x)
          # plt.imshow(x,cmap='gray')
          # plt.show()
        y=d-12
        td.append([x,y])
random.shuffle(td)
X=[]
Y=[]
for a1,a2 in td:
    X.append(a1)
    Y.append(a2)
print(X[0].shape)
X=np.array(X).reshape(-1,100,100)
Y=np.array(Y).reshape(-1,1)
#pickle.dump([X,Y],p1)
    