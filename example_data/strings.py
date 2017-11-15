print "Exercise 1"
s = "I love to write python"
for item in s:
    print item

print s[4]
print s[-1]
print len(s)
print s[0]
print s[0][0]
print s[0][0][0]

print "Exercise 2"

s = "I love to write python"

split_s = s.split()

print split_s

for word in split_s:
    if word.find("i") > -1:
        print "I have found 'i' in: '{0}' ".format(word)

print "End of exercises" # exercise 3 completed in linux

