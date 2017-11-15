
print "exercise 1"

a = [0,1,2]
b = a
print a, b
b[0] = "hello"
print a, b
a.append(3)
print a, b

print "exercise 2"

a = "can I change"
b = a
print a, b
b = "different"
print a, b

print "exercise 3"

import copy
a = range(3)
b = copy.deepcopy(a)
print a, b
b[0] = "hello"
print a, b