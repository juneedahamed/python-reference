import traceback
#Iterator should define __iter__ and __next__ methds
#Generator is a yeild function

class CounterIterator(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self


    def next(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            raise StopIteration


for c in CounterIterator(1,5): #Prints 2,3,4,5
    print "CounterIterator(1,5) ", c


i = iter(CounterIterator(1,6))
print i.next() #prints 2
print i.next() #prints 3
print i.next() #prints 4
print i.next() #prints 5
print i.next() #prints 6
#print i.next() #Will throw StopIteration


def CounterGenerator(start, end):
    for i in range(start, end):
        yield i

for c in CounterGenerator(1,5): #Prints 1, 2,3,4
    print "CounterGenerator(1,5) ", c

i = iter(CounterGenerator(1,6))
print i.next() #prints 2
print i.next() #prints 3
print i.next() #prints 4
print i.next() #prints 5
print i.next() #prints 6
try:
    print i.next() #Will throw StopIteration
except:
    traceback.print_exc()

#Generator expressions

squares = (x*x for x in range(2,10))  # Note Generator expr takes () not [] , these do not return lists
print squares.next()
for square in squares:
    print square

try:
    print squares.next() #Throws StopIteration
except StopIteration as si:
    print si
