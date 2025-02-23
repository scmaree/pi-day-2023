import time
import random
import os.path
import importlib
import pisano_example1

N = 400
M = 6000
ms = 1


def get_samples():
    """ Make a list of N samples chosen from [2, M]
    """
    random.seed(11235)  # Seed will be changed for the final scoring
    samples = random.sample(range(2, M+1), N)
    return sorted(samples)


def do_test(solution, samples, reference):
    """ Execute a function and compare the results with the reference
    """
    t0 = time.perf_counter()
    module = importlib.import_module(solution)
    func = module.get_pisano_numbers
    results = list(func(samples.copy()))
    t1 = time.perf_counter()
    runtime = (t1-t0) * 1000 * ms
    file_size = os.path.getsize(module.__file__)
    result = "PASS" if results == reference else "FAIL"
    return result, int(runtime), file_size


if __name__ == '__main__':
    samples = get_samples()
    reference = pisano_example1.get_pisano_numbers(samples)

    print("NAME\t\t\t\tRESULT\t  TIME\t  SIZE\t SCORE")
    if ms > 1:
        print(f"\t\t\t\t\t({ms} ms)\t  \t ")
    for solution in [
        "pisano_example1",
        "lookup_hex",
        "lookup_orthogonal",
        "compute_fast",
        "compute_short",
        "from math import isqrt,lcmNdef F(n,p=1):N while p<isqrt(n):N  p,c=p+1,0N  while not Oc+1N  if c:yield p**(c-1)*C(p)N if n>1:yield C(n)Ndef C(f):N c=k=l=1N while k or l!=1:k,l,c=l,(k+l)%f,c+1N return cNget_pisano_numbers=lambda l:[lcm(*F(m)) for m in l]"
        # "pisano_example2",
    ]:
        result, runtime, file_size = do_test(solution, samples, reference)
        score = runtime // ms + file_size
        print(f"{solution:30s}\t{result}\t{runtime:6d}\t{file_size:6d}\t{score:6d}")
