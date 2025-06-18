from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

locale.setlocale(locale.LC_ALL, 'nl_nl')

s = '20-8-1956'
dob = datetime.strptime(s, '%d-%m-%Y')

days = datetime.today() - dob

print(days)

print('Je bent geboren op', dob.strftime('%A %d %B %Y'))

delta = relativedelta(datetime.today(), dob)
print(delta.years)