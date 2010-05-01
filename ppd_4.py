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


class Carro(object):
    """
    >>> siena = Carro(10)
    >>> siena.combustivel
    0
    >>> siena.mover(10)
    'Sem gasolina? Como?'
    >>> siena.gasolina()
    0
    >>> siena.abastecer(2)
    >>> siena.gasolina()
    2
    >>> siena.mover(10)
    >>> siena.gasolina()
    1
    >>> siena.mover(200)
    Traceback (most recent call last):
    ...
    ValueError: precisa de mais gasolina do que tem
    """

    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def gasolina(self):
        return self.combustivel

    def abastecer(self, litros):
        self.combustivel += litros

    def mover(self, distancia):
        litros_por_km = 1./self.consumo
        if self.combustivel == 0:
            return 'Sem gasolina? Como?'
        elif litros_por_km * distancia > self.combustivel:
            raise ValueError("precisa de mais gasolina do que tem")

        self.combustivel -= int(litros_por_km * distancia)


class Vetor(object):
    """
    >>> v = Vetor(1, 1, 1)
    >>> w = Vetor(2, 2, 2)

    >>> v + w
    <Vetor(3, 3, 3)>

    >>> w - v
    <Vetor(1, 1, 1)>

    >>> v * w
    6

    >>> v * 2
    Traceback (most recent call last):
    ...
    NotImplementedError
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # O z entra no calculo da soma e da subtracao?
        return Vetor(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # O z entra no calculo da soma e da subtracao?
        return Vetor(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise NotImplementedError

    def __repr__(self):
        return u'<Vetor(%s, %s, %s)>' % (self.x, self.y, self.z)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
