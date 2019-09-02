from geometria.Figura import Figura
from math import pi


class Circulo(Figura):

    def __init__(self, radio=0):
        self.radio = radio

    def area(self):
        return pi * self.radio * self.radio

    def perimetro(self):
        return 2 * pi * self.radio
