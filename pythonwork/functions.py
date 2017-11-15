print "Exercises 2 and 3"

def calc_hypo(a,b):
    if type(a) not in (int, float) or type(b) not in (int,float):
        print "Bad arguement"
        return False
    elif a <= 0 or b <= 0:
        print "Bad arguement"
        return False
    else:
        hypo = (a**2 + b**2)**0.5
        return hypo

print calc_hypo(3,4)
print calc_hypo(0,-2)
print calc_hypo("hi","bye")

print "end of exercises 2 and 3"