#incrementor using lamda
def makeincrementor(n):  #closure
    print "make ", n #This is called first for makeincrementor
    return lambda x : x + n  # x is later passed

incr2 = makeincrementor(2)
incr10 = makeincrementor(10)

print incr2(10)
print incr10(10)


#incrementor using functools.partial
import functools
def makeincrementor(x, y):
    return x + y

incr2 = functools.partial(makeincrementor, 2)
incr10 = functools.partial(makeincrementor, 10)

print incr2(10)
print incr10(10)


#incrementor using closures

def makeincrementor(x):
    def _(y):
        return x + y
    return _

incr2 = makeincrementor(2)
incr10 =makeincrementor(10)

print incr2(10)
print incr10(10)

