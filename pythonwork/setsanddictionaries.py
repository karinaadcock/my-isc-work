print 'exercise 2'

band = ['mel', 'geri', 'victoria', 'mel', 'emma']

counts = {}

for name in band:
    if name not in counts:
         counts[name] = 1
    else:
         counts[name] += 1

for name in counts:
    print name, counts[name]

print 'exercise 3'

d = {'maggie':'uk', 'ronnie':'usa'}

print dir(d)
print d.items()
print d.keys()
print d.values()
print d.get("maggie","nowhere")
print d.get("ringo","nowhere")
res = d.setdefault("mikhail","ussr")
print res, d["mikhail"]