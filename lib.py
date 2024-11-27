def throwError(message):
    console.error(f"{message}\n\n")
    raise Exception(f"{message}")

def typeOf(input):
    return type(input)

class console:
    def log(input):
        print("\033[36m"+"[LOG]"+"\033[0m"+f" {input}")
    def info(input):
        print("\033[34m"+"[INFO]"+"\033[0m"+f" {input}")
    def debug(input):
        print("\033[32m"+"[DEBUG]"+"\033[0m"+f" {input}")
    def error(input):
        print("\033[31m"+"[ERROR]"+"\033[0m"+f" {input}")

class changeFrom:
    def __init__(self, input):
        self.inp = input
    def To(self, input):
        if(input == "Int"):
            try:
                self.inp = int(self.inp)
            except:
                throwError(f"{self.inp} Cannot Be Turned Into INT TYPE")
        elif(input == "Float"):
            try:
                self.inp = float(self.inp)
            except:
                throwError(f"{self.inp} Cannot Be Turned Into INT TYPE")
        elif(input == "String"):
            try:
                self.inp = str(self.inp)
            except:
                throwError(f"{self.inp} Cannot Be Turned Into INT TYPE")
        elif(input == "Bool"):
            try:
                self.inp = bool(self.inp)
            except:
                throwError(f"{self.inp} Cannot Be Turned Into INT TYPE")
        return self.inp

def Get(link):
    def decoratedGet(func):
        print(link)
        func()
    return decoratedGet

def OnError(fallback):
    def decoratedErrorHandler(func):
        try:
            func()
        except:
            fallback()
    return decoratedErrorHandler