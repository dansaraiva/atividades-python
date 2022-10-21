# Uma loja utiliza o código V para transação à vista e P para transação a prazo.
# Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:
# o valor total das compras à vista;
# o valor total das compras a prazo;
# o valor total das compras efetuadas; e
# o valor da primeira prestação das compras a prazo juntas, sabendo-se
# que serão pagas em três vezes

import os

c: str
compra: float
cv: float
cp: float
ct: float
compra = 0
cv = 0
cp = 0
c = ""

for n in range(1, 16):
    print(f"Dados da {n}ª venda")

    while (c != "V" and c != "P"):
        c = input(
            "Digite o código da compra (V - à vista ou P - a prazo): ").upper()
        if c == "V":
            compra = float(input("Digite o valor da compra: R$ "))
            cv = cv + compra
        elif c == "P":
            compra = float(input("Digite o valor da compra: R$ "))
            cp = cp + compra
    c = ""

    os.system("cls")

print(f"O valor total à vista: R$ {cv:.2f}")
print(f"O valor total a prazo: R$ {cp:.2f}")
print(f"O valor total das compras: R$ {cp + cv:.2f}")
print(
    f"O valor da primeira prestação das compras a prazo juntas: R$ {cp/3:.2f}")
