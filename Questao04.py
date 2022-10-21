# Faça um programa que receba um número, calcule e mostre a tabuada desse
# número.
n: int
num: int

num = int(input("Digite um número: "))
for n in range(0, 11):
    print(f"{num} x {n} = {num * n}")
