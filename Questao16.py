# Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas.
# Finalize digitando idade igual a zero.

idade: int
somaIdade: int
contIdade: int
mediaIdades: float

idade = 1
somaIdade = 0
contIdade = 0
mediaIdades = 0.0

while idade != 0:
    idade = int(input("Informe sua idade: "))

    somaIdade += idade
    contIdade += 1

mediaIdades = somaIdade / (contIdade - 1)

print("Média das idade digitadas: ", mediaIdades)
