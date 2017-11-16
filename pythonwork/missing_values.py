print "exercise 1"

import numpy.ma as MA
import numpy as np
marr = MA.masked_array(range(10),fill_value = -999)
print marr, marr.fill_value
marr [2] = MA.masked
print marr
print marr.mask
narr = MA.masked_where(marr > 6, marr)
print narr
x = MA.filled(narr)
print x
print type(x)

print "exercise 2"

m1 = MA.masked_array(range(1, 9))
print m1
m2 = m1.reshape(2,4)
print m2
m3 = MA.masked_greater(m2, 6)
print m3
print m3 * 100
res = m3 - np.ones((2,4))
print res
print type(res)