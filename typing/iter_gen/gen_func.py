import time
from datetime import datetime
def gen_fun():
    for i in range(5):
        time.sleep(1)
        yield i
    return None

for i in gen_fun():
    print(i, end=": ")
    print(datetime.now())
