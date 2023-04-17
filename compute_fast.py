import math
import functools as t


def F(n, p=1):
    while p < n**0.5:
        p, c = p+1, 0
        while not n % p:
            n, c = n//p, c+1
        if c:
            yield p**(c-1)*C(p)
    if n > 1:
        yield C(n)


@t.cache
def C(f, c=1, k=1, l=1):
    while k or l != 1:
        k, l, c = l, (k+l) % f, c+1
    return c


def get_pisano_numbers(l): return [math.lcm(*F(m)) for m in l]
