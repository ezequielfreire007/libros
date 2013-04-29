
def es_palindromo (seq):
    total = len (seq)
    for x in range (len (seq) / 2):
        if seq [x] != seq [total - x - 1]:
            return False
    return True

def es_palindromo_lento (seq):
    return seq == seq [::-1]

def palindromos (frase):
    palabras = frase.split (' ')
    palin_palab = dict ()
    for x in palabras:
        if x not in palin_palab:
            palin_palab [x] = es_palindromo (x)
    return es_palindromo (palabras), \
           palin_palab
