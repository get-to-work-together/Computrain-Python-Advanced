import pandas as pd

filename = 'ca-500.csv'

df = pd.read_csv(filename, sep=';')

print(df.loc[df['city']=='Montreal', ['first_name','last_name','city']])

print(df.loc[df['city']=='Montreal', ['first_name','last_name','city']].sort_values('last_name'))

df['name'] = df['first_name'] + ' ' + df['last_name']
print(df.loc[df['city']=='Montreal', ['first_name','last_name','name']])