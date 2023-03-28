This is my attempt at the challenge hosted by [vortechbv](https://github.com/vortechbv/pi-day-2023).

The Pisano period
=================

The Fibonacci series starts with [0, 1, 1, 2, ...] and has ever increasing numbers further down the series.
If you take these numbers modulo `n`, then the series will eventually become periodical.

This is called the [Pisano period][1] π(n). The series of Pisano numbers for n = [1, 2, 3, ...] is [A001175][2].


The challenge
-------------

Write a function `get_pisano_numbers()` in Python, which for a list of numbers `n` returns
the corresponding list of `π(n)`.  For example, `get_pisano_numbers([1,3])` would return `[1,8]`.

The winner is the function that is both the shortest and the fastest.


The rules
---------

 * The software used is Python 3.11.  Only modules from the standard library can be used, no numpy or other dependencies.
 * A submission should be a standalone `.py` file.
 * The score is the sum of the file size in bytes and the time to execute `get_pisano_numbers()` in miliseconds.
   Lower score wins.
 * Before scoring, the .py files are processed by `autopep8 --max-line-length 99999`, in order to limit
   tricks with removal of whitespace to some degree.
 * The input is a list of randomly chosen numbers from the range 2..6000.
   The list is 400 numbers long and the same for each submission.
 * The code is executed on a 16 core AMD CPU.


My Submissions
==============
Output of `test.py`:
```
    NAME                    RESULT    TIME    SIZE   SCORE
    pisano_example1         PASS         0   33004   33004
    lookup_hex              PASS         0   22573   22573
    lookup_orthogonal       PASS         1   18940   18941
    compute_fast            PASS        43     450     493
    compute_short           PASS        72     151     223
    def [...]               PASS        70      43     113
```

- `pisano_example1` (by vortechbv)  includes all Pisano periods for 1..6000 hardcoded in the source.
   This makes the execution very fast, but has a high score because of the file size.
- `lookup_hex` uses a hex-encoding of the list of all Pisano periods (from example 1). 
   Reduces size by ~33% at no noticeable cost.
- `lookup_orthogonal` uses a similar encoding, but reduces the size by first encoding the first bit of all 6000 Pisano periods; 
   then the second bit of all 6000 Pisano periods, etc... By doing so, we can exploit that the first Pisano periods are 
   smaller, and that all but `pisano_period(2)` are even.
- `compute_fast` exploits a prime factorization and the Chinese Remainder Theorem to efficiently compute Pisano periods.
- `compute_short` computes Pisano numbers in the least amount of code I could imagine.
- `def [...]` computes the Pisano numbers by using the observation that file size is independent of the file name, so it
   puts the algorithm of `compute_short` in the filename, with some tricks that pep8 would normally not allow, but  
   strings are not parsed by pep8; making it a bit of a loophole in the challenge. 


[1]: https://en.wikipedia.org/wiki/Pisano_period
[2]: https://oeis.org/A001175
