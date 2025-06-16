import pickle

filename = 'data.pickle'

with open(filename, 'rb') as f:
    data = pickle.load(f)

print(data)