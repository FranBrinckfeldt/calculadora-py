from geometria.Figura import Figura

class Triangulo(Figura):

    def __init__(self,base=0, altura=0, lado1=0, lado2=0):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2