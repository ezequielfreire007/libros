
from sucesos import sucesos
from itertools import islice

def algunospares (n, p):
    return map (int, islice (sucesos (1-p), n))

if __name__ == '__main__':
    print algunospares (5, .3)
