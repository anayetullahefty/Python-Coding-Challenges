# Taking input of 3 variables) as float using space
A, B, C = map(float, input().split(" "))

TRIANGULO = 0.5 * A * C
CIRCULO = 3.14159 * (C**2)
TRAPEZIO =  0.5 * ( A + B) * C
QUADRADO = (B**2)
RETANGULO = A * B

print("TRIANGULO: %.3f" %TRIANGULO)
print("CIRCULO: %.3f" %CIRCULO)
print("TRAPEZIO: %.3f" %TRAPEZIO)
print("QUADRADO: %.3f" %QUADRADO)
print("RETANGULO: %.3f" %RETANGULO)
