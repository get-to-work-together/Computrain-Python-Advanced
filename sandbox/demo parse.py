from parse import *

s = 'e-mail: peter@tip.nl'

result = parse('e-mail: {email}', s)

print(result['email'])

s = '20-8-1956'
result = parse('{day:d}-{month:d}-{year:d}', s)
print(result['day'],
      result['month'],
      result['month'])
