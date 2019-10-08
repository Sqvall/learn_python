import pickle

with open('serialize.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)
