# Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A — azul; P — preto; V — verde; e
# C — castanho) e a cor dos cabelos (P — preto; C — castanho; l — louro; e R — ruivo) de seis pessoas, e que
# calcule e mostre:
# a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg;
# a média das idades das pessoas com altura inferior a 1,50 m;
# a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas; e
# a quantidade de pessoas ruivas e que não possuem olhos azuis

idade: int
pessoasI50P60: int
somaIdade: int
qtdIdade: int
qtdOlhosAzuis: int
ruivosSemOlhosAzuis: int
peso: float
altura: float
peso60: float
corOlhos: str
corCabelos: str

somaIdade = 0
qtdIdade = 0
qtdOlhosAzuis = 0
ruivosSemOlhosAzuis = 0
pessoasI50P60 = 0

for n in range(1, 7):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite o altura: "))
    corOlhos = input(
        "Informe a cor dos olhos (A — azul; P — preto; V — verde; C — castanho): ")
    corCabelos = input(
        "Informe a cor dos cabelos (P — preto; C — castanho; L — Louro; R — ruivo): ")

    if idade > 50 and peso < 60:
        pessoasI50P60 = + 1
    if altura < 1.50:
        somaIdade += idade
        qtdIdade += 1
    if corOlhos == "A":
        qtdOlhosAzuis += 1
    if corCabelos == "R" and corOlhos != "A":
        ruivosSemOlhosAzuis += 1
print(
    f"Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg: {pessoasI50P60}")
print(
    f"Média das idades das pessoas com altura inferior a 1,50 m: {somaIdade/qtdIdade}")
print(
    f"Porcentagem de pessoas com olhos azuis entre todas as pessoas: {qtdOlhosAzuis/6*100:.2f}%")
print(
    f"Quantidade de pessoas ruivas e que não possuem olhos azuis: {ruivosSemOlhosAzuis}")
