#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Exercícios da primeira parte do livro Python para desenvolvedores
"""
import math

def celsius_para_fahrenheit(graus_celcius):
    """
    Função que converte temperatura em graus celcius para fahrenheit

    >>> celsius_para_fahrenheit(25)
    77.0
    """
    return 9/5.0 * graus_celcius + 32


def fahrenheit_para_celsius(graus_fahrenheit):
    """
    Função que converte temperatura em graus fahrenheit para celsius

    >>> fahrenheit_para_celsius(77)
    25.0
    """
    return 5.0/9 * (graus_fahrenheit - 32)


def is_prime(n):
    """
    Retorna verdadeiro se n for primo
    >>> is_prime(97)
    True

    e falso se n não for primo
    >>> is_prime(93)
    False
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        limit = int(math.sqrt(n))
        for x in range(2, limit):
            if n % x == 0:
                return False
        return True

def concatena_listas(lista_de_listas):
    """
    Recebe uma lista de listas e retorna uma única lista

    >>> concatena_listas([[1, 2, 3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]

    aceita listas de tamanhos arbitrários:

    >>> concatena_listas([[1, 2], [3, 4, 5, 6]])
    [1, 2, 3, 4, 5, 6]
    """
    return reduce(lambda x, y: x + y, lista_de_listas)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
