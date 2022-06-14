import csv

filename = 'ca-500.csv'
filename_out = 'out.tsv'

fieldnames = ('first_name','last_name','city','email')

with open(filename) as f:
    with open(filename_out, 'w') as f_out:

        reader = csv.DictReader(f, delimiter=';')
        writer = csv.DictWriter(f_out, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"', fieldnames=fieldnames)

        for d in reader:

            if d['city'] == 'Montreal':
                print(f"{d['first_name']:20} {d['last_name']:20} {d['city']:20} {d['email']:30}")

            writer.writerow({k:v for k,v in d.items() if k in fieldnames})


