import functools

#Decorator Funs with no arguments to dec or fun
def decNoArgs(original_fun_ref):

    @functools.wraps(original_fun_ref)
    def wrapper_to_original_fun():
            return original_fun_ref()
    return wrapper_to_original_fun

#Decorator Funs with fun arguments and no dec arguments
def decNoArgsToDecAndArgsToFun(original_fun_ref):

    @functools.wraps(original_fun_ref)
    def wrapper_to_original_fun(farg1, farg2):   # <--- These are fun arguments, 2 required
        return original_fun_ref(farg1, farg2)
    return wrapper_to_original_fun


#Decorator Funs with/without fun arguments and no dec arguments
def decNoArgsToDecAndArgsToFunGeneric(original_fun_ref):

    @functools.wraps(original_fun_ref)
    def wrapper_to_original_fun(*fnArgs, **fnKwArgs):   # <--- These are fun arguments - can pass *args and/or *kws
        return original_fun_ref(*fnArgs, **fnKwArgs)
    return wrapper_to_original_fun


##Decorator Funs with optional fun arguments and required dec arguments
def decArgsToDecAndArgsToFunGeneric(darg1, darg2):  #<-- forces a decorator with 2 args

    def external_wrap_to_to_original_fun(original_fun_ref):   #<---- Need this extra wrap as first wrap takes only args for dec

        @functools.wraps(original_fun_ref)
        def wrap_to_to_original_fun(*fnArgs, **fnKwArgs):   # <--- These are fun arguments
            print "Decorator got following args do something with it", darg1, darg2
            return original_fun_ref(*fnArgs, **fnKwArgs)
        return wrap_to_to_original_fun

    return external_wrap_to_to_original_fun


#Decorator Funs with optional fun arguments and optional dec arguments as kws
def decOptArgsAndOptFunArgs(original_fun_ref=None, **dargs):
    if original_fun_ref is None:
        return functools.partial(decOptArgsAndOptFunArgs, **dargs)

    @functools.wraps(original_fun_ref)
    def wrapper_to_original_fun(*fnArgs, **fnKwArgs):   # <--- These are fun arguments
        if dargs:
            print "Decorator got following kws for < %s > do something with it %s" %(original_fun_ref.__name__, dargs)
        return original_fun_ref(*fnArgs, **fnKwArgs)
    return wrapper_to_original_fun


#Define funs:
def funNoArgs():
    print "Hello from funNoArgs"

def funTwoArgs(arg1, arg2):
    print "Hello from funTwoArgs"
    print "\targ1=", arg1
    print "\targ2=", arg2

def funOneRqrdArgAndOneDflt(myarg1, mydefaultarg="i am default"):
    print "I am funOneRqrdArgAndOneDflt with one mandatory and one optional args"
    print "\tmyarg1 =", myarg1
    print "\tmydefaultarg =", mydefaultarg

def funArgsNKwds(*args, **kw):
    print "I am funArgsNKwds "
    print "\trcvd args = ", args
    print "\trcvd kwds =", kw

print "\n-----------Test decNoArgs --------"
test_funNoArgs = decNoArgs(funNoArgs)
test_funNoArgs()

print "\n-----------Test decNoArgsToDecAndArgsToFun --------"
test_funTwoArgs = decNoArgsToDecAndArgsToFun(funTwoArgs)
test_funTwoArgs("myfunarg1", "myfunarg2")


print "\n-----------decNoArgsToDecAndArgsToFunGeneric --------"
test_funNoArgs = decNoArgsToDecAndArgsToFunGeneric(funNoArgs)
test_funTwoArgs = decNoArgsToDecAndArgsToFunGeneric(funTwoArgs)
test_funOneRqrdArgAndOneDflt = decNoArgsToDecAndArgsToFunGeneric(funOneRqrdArgAndOneDflt)
test_funOneAllKwds =  decNoArgsToDecAndArgsToFunGeneric(funArgsNKwds)

test_funNoArgs()
test_funTwoArgs("One", "Two")
test_funOneRqrdArgAndOneDflt("Rqrd Arg")
test_funOneRqrdArgAndOneDflt("Rqrd Arg", "Overide Optional")

d = {"kw1":"One", "kw3":"Three"}
test_funOneAllKwds(d)
test_funOneAllKwds(*d)
test_funOneAllKwds(**d)


print "\n-----------Test deco with fun args and deco args--------"
test_funNoArgs = decArgsToDecAndArgsToFunGeneric("d1", "d2")(funNoArgs)
test_funTwoArgs = decArgsToDecAndArgsToFunGeneric("d1", "d2")(funTwoArgs)
test_funOneRqrdArgAndOneDflt = decArgsToDecAndArgsToFunGeneric("d1", "d2")(funOneRqrdArgAndOneDflt)
test_funOneAllKwds =  decArgsToDecAndArgsToFunGeneric("d1", "d2")(funArgsNKwds)

test_funNoArgs()
test_funTwoArgs("One", "Two")
test_funOneRqrdArgAndOneDflt("Rqrd Arg")
test_funOneRqrdArgAndOneDflt("Rqrd Arg", "Overide Optional")

d = {"kw1":"One", "kw3":"Three"}
test_funOneAllKwds(d)
test_funOneAllKwds(*d)
test_funOneAllKwds(**d)
test_funOneAllKwds(arg="myar1", *d)
test_funOneAllKwds(arg="myar1", **d)

print "\n-----------Test deco with opt fun args and  opt deco args--------"
test_funNoArgs = decOptArgsAndOptFunArgs()(funNoArgs)
test_funNoArgs()

test_funNoArgs = decOptArgsAndOptFunArgs(decarg1="One")(funNoArgs)
test_funNoArgs()

test_funTwoArgs = decOptArgsAndOptFunArgs()(funTwoArgs)
test_funTwoArgs("one", "two")

test_funTwoArgs = decOptArgsAndOptFunArgs(decarg1="One")(funTwoArgs)
test_funTwoArgs("one", "two")

@decOptArgsAndOptFunArgs
def test(a, b="def", c="red"):
    print "I am test function", a, b, c
test("abc")

print "-----------Test class method decorator --------"

class Test(object):
    @decOptArgsAndOptFunArgs
    def fun1(self):
        print "Test.fun1 called"

    @decOptArgsAndOptFunArgs
    def fun2(self, abc):
        print "test.fun2 called", abc

    @decOptArgsAndOptFunArgs
    def fun3(self, arg1="arg1", arg2="arg2"):
        print "Test.fun3 called"
        print arg1
        print arg2

    @decOptArgsAndOptFunArgs(arg1="one", arg2="two")
    def fun4(self):
        print "Test.fun4 called"

    @decOptArgsAndOptFunArgs(arg1="oneeee", arg2="nbbbbb")
    def fun5(self, abc):
        print "Test.fun4 called", abc


    def test(self):
        pass

t = Test()
t.fun1()
t.fun2("ABC")
t.fun3(arg1="one")
t.fun3(arg1="one", arg2="two")
t.fun4()
t.fun5(abc="ABC")
