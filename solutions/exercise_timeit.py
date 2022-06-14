from timeit import timeit

t1 = timeit('"-".join(str(n) for n in range(100))', number=10000)
print(t1)

t2 = timeit(lambda: "-".join(map(str, range(100))), number=10000)
print(t2)