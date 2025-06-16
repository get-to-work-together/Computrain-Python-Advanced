import pickle

data = {'name':'Peter', 'woonplaats':'Lhee', 'leeftijd':65}

filename = 'data.pickle'

with open(filename, 'wb') as f:
    pickle.dump(data, f)