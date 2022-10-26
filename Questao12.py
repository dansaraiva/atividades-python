# Faça um programa que receba dez números inteiros e mostre a quantidade de números
# primos dentre os números que foram digitados.
import math

num: int
contPrimo: int
qtdPrimo: int

num = 0
contPrimo = 0
qtdPrimo = 0

for n in range(1, 4):
    num = int(input("Digite número: "))

    for m in range(2, int(math.sqrt(num)+1)):
        if num % m == 0:
            contPrimo += 1

    if contPrimo == 0:
        qtdPrimo += 1

    contPrimo = 0

print(f"Quantidade de números primos: {qtdPrimo}")
