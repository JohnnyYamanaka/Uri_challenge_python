A, B, C = list(map(float,input().split(" ")))
pi = 3.14159

TRIANGULO_AREA = (A * C) / 2

CIRCULO_AREA = pow(C,2) * pi

TRAPEZIO_AREA = ((A + B) * C) / 2

QUADRADO_AREA = pow(B, 2)

RETANGULO_AREA = A * B


print("TRIANGULO: %.3f" % TRIANGULO_AREA)
print("CIRCULO: %.3f" % CIRCULO_AREA)
print("TRAPEZIO: %.3f" % TRAPEZIO_AREA)
print("QUADRADO: %.3f" % QUADRADO_AREA)
print("RETANGULO: %.3f" % RETANGULO_AREA)