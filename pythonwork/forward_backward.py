forward = []
backward = []
values = ["a", "b", "c"]

for item in values:
    forward.append(item)
    backward.insert(0, item)

print "Forward is:", forward
print "Backward is:", backward
print forward.reverse()
forward = forward[::-1]
print forward == backward