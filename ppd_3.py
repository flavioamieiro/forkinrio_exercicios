from math import ceil, sqrt


def prime_generator():
    """
    An infinite prime numbers generator

    >>> g = prime_generator()
    >>> for i in range(25):
    ...     print g.next(),
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 \
59 61 67 71 73 79 83 89 97


    it does not have a limit, so if you don't want
    an infinite loop, you have to explicitly break
    out of your loop:

    >>> for i in prime_generator():
    ...     if i > 100:
    ...         break
    ...     print i,
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 \
59 61 67 71 73 79 83 89 97
    """

    n = 1
    while True:
        if n == 1:
            is_prime = False
        elif n == 2:
            is_prime = True
        else:
            is_prime = True
            limit = int(ceil(sqrt(n))) + 1
            for x in range(2, limit):
                if n % x == 0:
                    is_prime = False

        if is_prime:
            yield n

        n += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
