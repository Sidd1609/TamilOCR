import cv2
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
X=cv2.imread('a2.jpg')
X = cv2.cvtColor(X, cv2.COLOR_BGR2GRAY)
(thresh, X) = cv2.threshold(X, 127, 255, cv2.THRESH_BINARY)
f=0
jl=[]
il=[]
#print(X)
for i in range(X.shape[0]):
    t=X[i]
    for j in range(X.shape[1]):
        if(t[j]==0):
            il.append(i)
            break
            
##print(X.shape)
#print(il)
Y=X[il[0]-5:il[len(il)-1]+5]
for j in range(Y.shape[1]):
    t=Y[:,j]
    for i in range(Y.shape[0]):
        if(t[i]==0):
            jl.append(j)
            break
jll=[]
jll.append(jl[0])
for i in range(1,len(jl)):
    if(abs(jl[i]-jl[i-1])>3):
        jll.append(jl[i-1])
        jll.append(jl[i])
jll.append(jl[len(jl)-1])
##print(jll)
##print(jl)
##print(len(jll))
im=[]
for i in range(int(len(jll)/2)):
    im.append(Y[:,jll[2*i]-5:jll[2*i+1]+5])
print(len(im))
for i in range(len(im)):
    cv2.imshow(f'im{i}',im[i])
    cv2.imwrite(f'im{i}.jpg',im[i])
        
#cv2.imshow('2',Y)
