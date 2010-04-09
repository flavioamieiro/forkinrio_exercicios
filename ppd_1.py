#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Exercícios da primeira parte do livro Python para desenvolvedores
"""
import math
import operator

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
    return reduce(operator.add, lista_de_listas)


def calculate_with_values(dicionario):
    """
    Dado um dicionário, retorna a soma, média e variação dos valores
    (entendi variação como a diferença entre o menor e o maior elemento)

    >>> calculate_with_values({'a': 1, 'b': 2, 'c': 3})
    (6, 2, 2)

    >>> calculate_with_values({'a': 10, 'b': 32.5, 'c': 23, 'd': 41})
    (106.5, 26.625, 31)
    """
    lista_de_valores = dicionario.values()
    soma = sum(lista_de_valores)
    media = soma / len(lista_de_valores)
    variacao = max(lista_de_valores) - min(lista_de_valores)

    return soma, media, variacao


def inverte_palavras(frase):
    """
    Dada uma frase, retorna outra com as letras das palavras invertidas

    >>> inverte_palavras('python para desenvolvedores')
    'nohtyp arap serodevlovnesed'
    """
    return ' '.join([palavra[::-1] for palavra in frase.split()])


def ordena(dados, chave=0, reverso=False):
    """
    Ordena uma lista de tuplas dada uma chave

    >>> ordena([(1, 2, 3), (2, 1, 3), (3, 2, 1)])
    [(1, 2, 3), (2, 1, 3), (3, 2, 1)]

    >>> ordena([(1, 2, 3), (2, 1, 3), (3, 2, 1)], 0, True)
    [(3, 2, 1), (2, 1, 3), (1, 2, 3)]

    >>> ordena([(1, 2, 3), (2, 1, 3), (2, 3, 1)], 1)
    [(2, 1, 3), (1, 2, 3), (2, 3, 1)]

    >>> ordena([(1, 2, 3), (2, 1, 3), (2, 3, 1)], 1, True)
    [(2, 3, 1), (1, 2, 3), (2, 1, 3)]
    """
    dados.sort(cmp=lambda x, y: cmp(x[chave], y[chave]), reverse=reverso)
    return dados


if __name__ == '__main__':
    import doctest
    doctest.testmod()
