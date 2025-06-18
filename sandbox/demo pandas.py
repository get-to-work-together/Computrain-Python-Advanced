import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

filename = '../data/ca-500.csv'
df = pd.read_csv(filename, sep=';')

print(df.info())

selected = df[['first_name','last_name','city','email']].query('city=="Montreal"')

df['province'].value_counts().plot(kind='barh')
plt.show()
