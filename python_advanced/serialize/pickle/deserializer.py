import pickle
from python_advanced.serialize.pickle.serializer import Person

with open('serialize.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)
