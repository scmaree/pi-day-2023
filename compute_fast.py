import math
n, q = 5988, [2]
s = [True]*n
for i in range(3, int(n**0.5)+1, 2):
    if s[i]:
        s[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
q += [i for i in range(3, n, 2) if s[i]]


def C(m, f, d=-1, c=1, k=1, l=1):
    while not m % f:
        m, d = m//f, d+1
    while k or l != 1:
        k, l, c = l, (k+l) % f, c+1
    return f**d*c


def get_pisano_numbers(l): return [math.lcm(*[C(m, f) for f in [p for p in q if not m % p]]) for m in l]
