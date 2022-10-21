# Uma companhia de teatro deseja montar uma série de espetáculos.
# A direção calcula que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos,
# e que as despesas serão de R$ 200,00. Diminuindo-se em R$ 0,50 o preço dos
# ingressos, espera-se que as vendas aumentem em 26 ingressos.
# Faça um programa que escreva uma tabela de valores de lucros esperados em
# função do preço do ingresso, fazendo-se variar esse preço de R$ 5,00 a
# R$ 1,0, de R$ 0,50 em R$ 0,50. Escreva, ainda, para cada novo preço de
# ingresso, o lucro máximo esperado, o preço do ingresso e a quantidade de
# ingressos vendidos para a obtenção desse lucro.

precoIngresso: float
despesas: float
lucro: float
qtdIngresso: int

precoIngresso = 5.00
qtdIngresso = 120
despesas = 200.00

while precoIngresso >= 1.00:
    lucro = qtdIngresso * precoIngresso - despesas
    print(f"|Preço: \t\t|R$ {precoIngresso:.2f}")
    print(f"|Lucro: \t\t|R$ {lucro:.2f} ")
    print(f"|Ingressos vendidos: \t|{qtdIngresso}")
    print("-----------------------------------")
    precoIngresso = precoIngresso - 0.50
    qtdIngresso = qtdIngresso + 26
