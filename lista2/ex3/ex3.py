# Exercício 3

temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

for temperatura in temperaturas:
    z = (temperatura - media) / desvio
    print(temperatura, "->", z, "->", abs(z))
