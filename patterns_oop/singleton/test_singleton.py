from singleton import singleton

x = singleton.Singleton()
x2 = singleton.Singleton()
x.q = 2
print(x.__dict__, x2.__dict__)