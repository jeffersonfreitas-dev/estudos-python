class Triangulo:
    #construtor
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

#instanciar objeto
t1 = Triangulo(1, 2, 3)

print(f"Triangulo size: {t1.lado1}, {t1.lado2}, {t1.lado3}")