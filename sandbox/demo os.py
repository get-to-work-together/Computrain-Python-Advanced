import os

print(os.getcwd())
os.chdir('../data')
print(os.getcwd())

with open('demo.txt') as f:
    print(f.read())

for item in os.listdir():
    if item.endswith('.csv'):
        print('Processing ...', item)
        print(f'Processing ... {item}')
        print('Processing ... %s' % item)
        print('Processing ... {}'.format(item))
        print('Processing ... ' + item)
