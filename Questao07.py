#Faça um programa que receba a idade, a altura e o peso de cinco 
#pessoas, calcule e mostre:
#a quantidade de pessoas com idade superior a 50 anos;
#a média das alturas das pessoas com idade entre 10 e 20 anos;
#a porcentagem de pessoas com peso inferior a 40 kg entre todas as 
#pessoas analisadas.
import os

idade: int; idade50: int; alturaEntre10e20: int; peso40: int; qtdCad: int
altura: float; peso: float; somaAltura: float

idade50 = 0
altura = 0
somaAltura = 0
alturaEntre10e20 = 0
peso40 = 0
qtdCad = 0
os.system("cls")
qtdCad = int(input("Informe a quantidade de cadastros a serem realizados: "))

for n in range(1, qtdCad + 1):
    print(f"Informe os dados para {qtdCad} pessoas!")
    print(f"Informe os dados para {n}ª pessoa:")

    idade = int(input("Informe idade: "))
    altura = float(input("Informe altura: "))
    peso = float(input("Informe peso: "))
    os.system("cls")
    if idade > 50:
        idade50 += 1
    if idade >= 10 and idade <= 20:
        somaAltura += altura
        alturaEntre10e20 += 1
    if peso < 40:
        peso40 += 1

print(f"Existem {idade50} pessoas com idade superior a 50 anos.")
if  alturaEntre10e20 <= 0:
    print("Não foram informadas pessoas com média de alturas entre 10 e 20 anos")
else:
    print(f"A média das alturas entre 10 e 20 anos é de {somaAltura/alturaEntre10e20:.2f}m")
print(f"% pessoas com peso inferior a 40kg: {peso40/qtdCad*100}%")

