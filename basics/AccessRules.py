class AccessRules(object):

    def __init__(self):
        self._oneUScore  = 100 #This just convention states this is
                               #not part of api to be accessed outside of
                               #class. However still accessable

        self.__twoUScore = 200 #This is not accessible from outside of class
                               #This is not accessable for derived classes also


        self.__fourUScore__ = 300 #This is bad, this convention is reserved for
                                  #internal python only

    def getTwoScore(self): #Access method for private __twoUScore
        return self.__twoUScore

a = AccessRules()

print a._oneUScore
print a.__fourUScore__
try:
    print a.__twoUScore  #Exception not accessible
except Exception as e:
    print e

print a.getTwoScore()


class SubClass(AccessRules):

    def show(self):
        print self._oneUScore
        print self.__fourUScore__

        try:
            print self.__twoUScore #Exception No atttribute
        except Exception as e:
            print e

        print self.getTwoScore() #Access __twoUScore

SubClass().show()

