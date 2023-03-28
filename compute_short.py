def p(m, c=1, k=1, n=1):
    while k or n != 1:
        k, n, c = n, (k+n) % m, c+1
    return c


def get_pisano_numbers(l): return [p(n) for n in l]
