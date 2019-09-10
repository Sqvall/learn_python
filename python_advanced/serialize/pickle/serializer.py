import pickle
from reprlib import recursive_repr


class Person(object):
    def __init__(self, name, age, siblings=None):
        self.name = name
        self.age = age
        self.siblings = siblings or []

    @recursive_repr()
    def __repr__(self):
        return 'Person({name!r}, {age!r}, {siblings!r})'.format_map(self.__dict__)

    @staticmethod
    def make_siblings(first, second):
        first.siblings.append(second)
        second.siblings.append(first)


josh = Person('Josh', 23)
anna = Person('Anna', 20)

Person.make_siblings(josh, anna)

with open('serialize.pkl', 'wb') as f:
    pickle.dump((josh, anna), f)
