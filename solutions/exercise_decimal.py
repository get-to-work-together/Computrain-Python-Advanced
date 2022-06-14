from decimal import Decimal

totaal = 0
aantal = 0

for n1 in range(1, 10):
    for n2 in range(1, 10):

        f1 = n1 / 10
        f2 = n2 / 10

        q1 = f1 + f2

        print('floats', f'{f1} + {f2} = {q1}')

        d1 = Decimal(str(f1))
        d2 = Decimal(str(f2))

        q2 = float(d1 + d2)

        print('Decimals', f'{d1} + {d2} = {q2}')

        totaal += 1
        if q1 != q2:
            aantal += 1

print(aantal, totaal, aantal/totaal*100, '%')