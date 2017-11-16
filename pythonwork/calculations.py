print "exercise 1"

import numpy as np

a = np.array([range(4),range(10,14)])
b = np.array([2,-1,1,0])
print a * b

b1 = b * 100
b2 = b * 100.0
print b1, b2

print b1 == b2

print b1.dtype, b2.dtype

print "exercise 2"

arr = np.arange(10)

print arr < 3

print np.less(arr,3)

condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)
print new_arr

print "exercise 3"

def calcMagnitude(u, v, minmag = 0.1): 
   mag = ((u**2) + (v**2))**0.5
   output = np.where(mag > minmag, mag, minmag)
   return output

u = np.array([[4, 5, 6], [2, 3, 4]])
v = np.array([[2,2,2], [1,1,1]])
print calcMagnitude (u, v)

u = np.array([[4, 5, 0.01], [2,3,4]])
v = np.array([[2,2,0.03], [1, 1, 1]])
print calcMagnitude (u, v)


