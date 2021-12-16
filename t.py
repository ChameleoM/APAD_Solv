import pickle

with open('pcs.pk', 'r+b') as f:
    a = pickle.load(f)
f.close()

print(a)