#-*- coding: utf-8 -*-
import sys
from math import ceil, sqrt
from itertools import ifilterfalse, count


def prime_generator():
    """
    An infinite prime numbers generator

    >>> g = prime_generator()
    >>> for i in range(25):
    ...     print g.next(),
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


    it does not have a limit, so if you don't want
    an infinite loop, you have to explicitly break
    out of your loop:

    >>> for i in prime_generator():
    ...     if i > 100:
    ...         break
    ...     print i,
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
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

def one_line_prime_generator():
    """
    An infinite prime numbers generator implemented in one line

    >>> g = one_line_prime_generator()
    >>> for i in range(25):
    ...     print g.next(),
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


    it does not have a limit, so if you don't want
    an infinite loop, you have to explicitly break
    out of your loop:

    >>> for i in one_line_prime_generator():
    ...     if i > 100:
    ...         break
    ...     print i,
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


    O 100o primo deve ser 541
    >>> g = one_line_prime_generator()
    >>> for i in range(100):
    ...     a = g.next()
    >>> print a
    541
    """
    # Esse filterfalse tira do generator os numeros que tem divisores
    # maiores que 1
    return ifilterfalse(
        # Esse lambda retorna uma lista com os divisores maiores que 1
        # do numero em questao (com caso especial para o 2)
        lambda n:
            False if n == 2 else [
                x for x in range(2, int(ceil(sqrt(n)))+1) if n % x == 0
            ]
        ,
        count(2)
    )

def rgb_range():
    for r in range(256):
        for g in range(256):
            for b in range(256):
                yield (r, g, b)

def rgb_xrange():
    for r in xrange(256):
        for g in xrange(256):
            for b in xrange(256):
                yield (r, g, b)

def read_csv(file):
    """
    Lê um csv e retorna uma lista de tuplas, onde cada elemento é um campo do csv

    >>> print read_csv('arquivo.csv')
    [('1', '2', '3', '4'), ('favorite color', 'yellow')]

    Imprime na tela alguma coisa e sai em caso de erro:
    >>> read_csv('arquivo_que_nao_existe.csv')
    Traceback (most recent call last):
        ...
    SystemExit: 1

    """

    try:
        with open(file, 'r') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]

        return [tuple(l.split(',')) for l in lines]
    except:
        sys.stderr.write("Ops\n")
        sys.exit(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
