class Test:
    def __init__(self):
        self.__private = 100
        self.__priv()
    
    def debug(self):
        print(self.__private)

    def __priv(self):
        print("priv")

t = Test()
t.debug()
t.__private = 200
t.debug()
print(t.__private)
# t._Test__priv()