# Uma empresa fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de
# um novo produto lançado. Para isso, forneceu o sexo do entrevistado e sua
# resposta (S — sim; ou N — não). Sabe-se que foram entrevistadas dez pessoas.
# Faça um programa que calcule e mostre:
# o número de pessoas que responderam sim;
# o número de pessoas que responderam não;
# o número de mulheres que responderam sim; e
# a percentagem de homens que responderam não, entre todos os homens analisados.

sexo: str
resposta: str
totalSim: int
totalNao: int
mulheresSim: int
homensNao: int
homensSim: int
homensTotal: int
perHomens: float

sexo = ""
resposta = ""
totalSim = 0
mulheresSim = 0
totalNao = 0
perHomens = 0
homensNao = 0
homensSim = 0
homensTotal = 0

for n in range(1, 11):
    sexo = input("Digite seu sexo (F - Feminino ou M - Masculino): ")
    resposta = input("Qual sua resposta? (S — sim; ou N — não)")

    if resposta == "S":
        totalSim += 1
        if sexo == "F":
            mulheresSim += 1
        else:
            homensSim += 1

    if resposta == "N":
        totalNao += 1
        if sexo == "M":
            homensNao += 1

homensTotal = homensNao + homensSim
perHomens = homensNao / homensTotal * 100

print("O número de pessoas que responderam sim: ", totalSim)
print("O número de pessoas que responderam não: ", totalNao)
print("O número de mulheres que responderam sim: ", mulheresSim)
print("O percentagem de homens que responderam não, entre homens: ", perHomens)
