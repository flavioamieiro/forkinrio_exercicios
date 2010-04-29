class Quadrado(object):
    """
    >>> quadrado = Quadrado(2)
    >>> quadrado.get_lado()
    2
    >>> quadrado.set_lado(3)
    >>> quadrado.get_lado()
    3
    >>> quadrado.get_area()
    9
    """

    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, lado):
        self.lado = lado

    def get_area(self):
        return self.lado ** 2


class Lista(list):
    def sem_repeticao(self):
        """
        >>> lista = Lista((1, 2, 3, 2))
        >>> lista.sem_repeticao()
        [1, 2, 3]
        """
        #Na marreta vale?
        return list(set(self))

    def sem_repeticao_nem_marreta(self):
        """
        >>> lista = Lista((1, 2, 3, 2))
        >>> lista.sem_repeticao_nem_marreta()
        [1, 2, 3]
        """
        resultado = []
        for value in self:
            if value not in resultado:
                resultado.append(value)
        return resultado



if __name__ == '__main__':
    import doctest
    doctest.testmod()
