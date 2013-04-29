from itertools import chain

def gen_memoizer (generator):
    res = []
    gen = generator ()
    def newvalues ():
        while True:
            x = gen.next ()
            res.append (x)
            yield x
    return lambda: chain (res, newvalues ())

if __name__ == '__main__':
    from primos import sieve
    from itertools import islice
    
    memo_sieve = gen_memoizer (sieve)

    p1 = memo_sieve ()
    p2 = memo_sieve ()
    print list (islice (p1, 10))
    print list (islice (p2, 10))
