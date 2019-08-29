class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton().getInstance()  ## class initialized, but object not created
# print("Object created", Singleton.getInstance())  # Object gets created here
s1 = Singleton()  ## instance already created
s.z = 2
print(s1.__dict__, s.__dict__)
print(s1.getInstance().__dict__, s.__dict__)
