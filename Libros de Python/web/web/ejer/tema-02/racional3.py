
class Racional (object):
    
    __slots__ = 'num', 'den'

    def __init__ (self, num = 0, den = 1, *a, **k):
        super (Racional, self).__init__ (*a, **k)
        self.num = num
        self.den = den

    def __add__ (a, b):
        return Racional (b.num + a.num, b.den) \
               if b.den == a.den else \
               Racional (b.num * a.den + a.num * b.den,
                         b.den * a.den)

    def __sub__ (a, b):
        return a + Racional (-1) * b

    def __mul__ (a, b):
        return Racional (a.num * b.num,
                         a.den * b.den)

    def __div__ (a, b):
        return a * Racional (b.den, b.num)

    def __str__ (self):
        return '(%i/%i)' % (self.num, self.den)

    def entero (self):
        q, r = divmod (self.num, self.den)
        if r:
            raise ValueError, "El Racional no es entero"
        return q
    entero = property (entero)

if __name__ == '__main__':
    print "Test1: ", Racional (9, 3).entero
    try:
        print Racional (9, 4).entero
    except ValueError, err:
        print err

