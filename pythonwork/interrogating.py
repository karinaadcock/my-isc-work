print "exercise 1"

import numpy as np

arr = np.array([range(4), range(10,14)])

print arr

print arr.shape
print np.shape(arr)
print arr.size
print np.size(arr)
print arr.max()
print arr.min()

print "exercise 2"

print np.reshape(arr, (2,2,2))
print np.transpose(arr)
print np.ravel(arr)
b = arr.astype(np.float64)
print b