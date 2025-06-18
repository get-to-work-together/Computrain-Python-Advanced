filename = '../data/demo_data.txt'

with open(filename) as f:

    headers = f.readline().strip().split(',')
    print(headers)

    for line in f:
        line = line.strip()
        naam, woonplaats = line.split(',')
        if 'a' in naam:
            print(f'{naam} - {woonplaats}')
