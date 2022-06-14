import time
from threading import Thread

def myfunc(i):
    for counter in range(5):
        print(f'{i} > {counter}')
        time.sleep(1)

    # print("sleeping 5 sec from thread %d" % i)
    # time.sleep(5)
    # print("finished sleeping from thread %d" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
