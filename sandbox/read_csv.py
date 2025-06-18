filename = '../data/ca-500.csv'

try:
    with open(filename) as f:

        headers = f.readline().strip().split(';')
        print(headers)

        for line in f:
            values = line.strip().split(';')

            d = dict(zip(headers, values))

            if d['city'].lower() in ('montreal', 'vancouver'):
                print(f'{d['first_name']:20} {d['last_name']:20} {d['city']:20} {d['email']}')

except FileNotFoundError:
    print(f'File not found: {filename}')
