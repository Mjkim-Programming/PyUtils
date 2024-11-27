from lib import *;

console.log(typeOf(changeFrom("3").To("Int")))

@Get("/")
def test():
    print("a")

def errorHandler():
    throwError("ASDF")

@OnError(errorHandler)
def failingFunc():
    a = int("3a")