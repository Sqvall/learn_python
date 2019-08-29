class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", id(s))
s1 = Singleton()
print("Object created", id(s1))
s.x = 2
print(s.__dict__)
print(s1.__dict__)
