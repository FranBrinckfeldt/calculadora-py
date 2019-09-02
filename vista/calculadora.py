from geometria.Circulo import Circulo
from geometria.Triangulo import Triangulo

while True:
    print("""¿Qué cálculo desea realizar?
    1: Sumar
    2: Restar
    3: Multiplicar
    4: Dividir
    5: Calcular el área
    6: Calcular el perimetro
    0: Salir""")

    while True:
        try:
            opcion = int(input())
            if (opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 0):
                break
            else:
                print("Ingrese una opción válida")
        except:
            print("Ingrese una opción válida")
            int(input())

    if (opcion == 1):

        while True:
            try:
                cantidad = int(input("¿Cuántos números desea ingresar?: "))
                break
            except:
                print("Ingrese una cantidad válida")

        numeros = []

        for i in range(cantidad):
            while True:
                try:
                    numeros.append(int(input("Ingrese un número: ")))
                    break
                except:
                    print("Ingrese un número válido")

        suma = 0

        for numero in numeros:
            suma = suma + numero

        print(suma)

    if (opcion == 2):

        while True:
            try:
                cantidad = int(input("¿Cuántos números desea ingresar?: "))
                break
            except:
                print("Ingrese una cantidad válida")

        numeros = []

        for i in range(cantidad):
            while True:
                try:
                    numeros.append(int(input("Ingrese un número: ")))
                    break
                except:
                    print("Ingrese un número válido")

        resta = numeros[0]
        contador = 0

        for numero in range (1, len(numeros)):
            resta = resta - numeros[contador+1]
            contador = contador + 1

        print(resta)

    if (opcion == 3):

        while True:
            try:
                cantidad = int(input("¿Cuántos números desea ingresar?: "))
                break
            except:
                print("Ingrese una cantidad válida")

        numeros = []

        for i in range(cantidad):
            while True:
                try:
                    numeros.append(int(input("Ingrese un número: ")))
                    break
                except:
                    print("Ingrese un número válido")

        multiplicacion = numeros[0]
        contador = 0

        for numero in range (1, len(numeros)):
            multiplicacion = multiplicacion * numeros[contador+1]
            contador = contador + 1

        print(multiplicacion)

    if (opcion == 4):

        while True:
            try:
                cantidad = int(input("¿Cuántos números desea ingresar?: "))
                break
            except:
                print("Ingrese una cantidad válida")

        numeros = []

        for i in range(cantidad):
            while True:
                try:
                    numeros.append(int(input("Ingrese un número: ")))
                    break
                except:
                    print("Ingrese un número válido")

        division = numeros[0]
        contador = 0

        for numero in range(1, len(numeros)):
            division = division / numeros[contador + 1]
            contador = contador + 1

        print(division)

    if (opcion == 5):

        print("""¿De qué figura desea calcular el área?
        1: Círculo
        2: Triángulo""")

        while True:
            try:
                figura = int(input())
                if (figura == 1 or figura == 2):
                    break
                else:
                    print("Ingrese una opción válida")
            except:
                print("Ingrese una opción válida")
                int(input())

        if (figura == 1):
            while True:
                try:
                    radio = int(input("Ingrese el radio del círculo: "))
                    break
                except:
                    print("Ingrese un número válido")

            c = Circulo(radio)
            print(c.area())

        if (figura == 2):
            while True:
                try:
                    base = int(input("Ingrese la base del triángulo: "))
                    break
                except:
                    print("Ingrese un número válido")

            while True:
                try:
                    altura = int(input("Ingrese la altura del triángulo: "))
                    break
                except:
                    print("Ingrese un número válido")

            t = Triangulo(base, altura, 0, 0)
            print(t.area())

    if (opcion == 6):

        print("""¿De qué figura desea calcular el área?
            1: Círculo
            2: Triángulo""")

        while True:
            try:
                figura = int(input())
                if (figura == 1 or figura == 2):
                    break
                else:
                    print("Ingrese una opción válida")
            except:
                print("Ingrese una opción válida")
                int(input())

        if (figura == 1):
            while True:
                try:
                    radio = int(input("Ingrese el radio del círculo: "))
                    break
                except:
                    print("Ingrese un número válido")

            c = Circulo(radio)
            print(c.perimetro())

        if (figura == 2):

            while True:
                try:
                    base = int(input("Ingrese la base del triángulo: "))
                    break
                except:
                    print("Ingrese un número válido")

            while True:
                try:
                    lado1 = int(input("Ingrese el tamaño de un lado del triángulo: "))
                    break
                except:
                    print("Ingrese un número válido")

            while True:
                try:
                    lado2 = int(input("Ingrese el tamaño del otro lado del triángulo: "))
                    break
                except:
                    print("Ingrese un número válido")

            t = Triangulo(base, 0, lado1, lado2)
            print(t.perimetro())

    if (opcion == 0):
        break