import re

filename = 'ca-500.csv'

with open(filename) as f:

    headers = f.readline().rstrip().split(';')
    print(headers)

    for line in f:
        columns = line.rstrip().split(';')

        d = dict(zip(headers, columns))

        # if d['city'] == 'Montreal':
        #     print(f"{d['first_name']:20} {d['last_name']:20} {d['city']:20} {d['email']:30}")

        # if d['city'] in {'Montreal', 'Toronto'}:
        #     print(f"{d['first_name']:20} {d['last_name']:20} {d['city']:20} {d['email']:30}")

        if re.search('yahoo.com$', d['email']):
            print(f"{d['first_name']:20} {d['last_name']:20} {d['city']:20} {d['email']:30}")

