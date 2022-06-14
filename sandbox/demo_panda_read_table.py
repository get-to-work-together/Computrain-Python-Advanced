import pandas as pd

url = 'https://nl.wikipedia.org/wiki/Lijst_van_E-nummers'

tables = pd.read_html(url)

df = tables[1]

print(df)

df.to_csv('conserveringsmiddelen.csv')