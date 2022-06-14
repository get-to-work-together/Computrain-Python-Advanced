import os

dirname = '/users/peter'

listing = os.listdir(dirname)

for entry in sorted(listing, key = lambda e: e.lower()):
    if not entry.startswith('.'):
        print(entry)