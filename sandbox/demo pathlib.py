from pathlib import Path

filename = Path('..') / 'data' / 'ca_500.csv'

print(filename)

for item in Path('..').glob('**/*.py'):
    print(item)