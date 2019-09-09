from patterns_oop.singleton.refactoring_guru import Singleton

x = Singleton()
x2 = Singleton()
x.q = 2
print(x.__dict__, x2.__dict__)