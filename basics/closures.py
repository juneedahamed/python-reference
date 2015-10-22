#Wrapping a function within another is called closure

def make_log(level):
    def _(message): # _ is just used can use a name as well
        print("{}: {}".format(level, message))
    return _

loginfo = make_log("info")
logwarn = make_log("warn")
logerr = make_log("error")


loginfo("The info message")
logwarn("The warn message")
logerr("The error message")


from functools import partial
def logit(level, message):
    print("{}: {}".format(level, message))

linfo = partial(logit, "info")
lwarn = partial(logit, "warn")
lerror = partial(logit, "error")

linfo("Test")
lwarn("Test")
lerror("Test")
