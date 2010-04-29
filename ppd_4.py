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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
