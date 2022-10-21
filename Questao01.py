# Faça um programa que leia cinco grupos de quatro valores (A, B, C, D) e
# mostre-os na ordem lida.
# Em seguida, organize-os em ordem crescente e decrescente

a: int
b: int
c: int
d: int
n: int
m1: int
m2: int
m3: int
m4: int

m1 = 0
m2 = 0
m3 = 0
m4 = 0

for n in range(1, 6):
    
    print(f"Digite valores para grupo {n}: ")    
    a = int(input("Digite valor para A: "))
    b = int(input("Digite valor para B: "))
    c = int(input("Digite valor para C: "))
    d = int(input("Digite valor para D: "))
    
    if a > b and a > c and a > d:
        m1 = a
        if b > c and b > d:
            m2 = b
            if c > d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        elif c > b and c > d:
            m2 = c
            if b > d:
                m3 = b
                m4 = d
            else:
                m3 = d
                m4 = b
        else:
            m2 = d
            if b > c:
                m3 = b
                m4 = c
            else:
                m3 = c
                m4 = b
    if b > a and b > c and b > d:
        m1 = b
        if a > c and a > d:
            m2 = a
            if c > d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        elif c > a and c > d:
            m2 = c
            if a > d:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
        else:
            m2 = d
            if a > c:
                m3 = a
                m4 = c
            else:
                m3 = c
                m4 = a
    if c > a and c > b and c > d:
        m1 = c
        if a > b and a > d:
            m2 = a
            if b > d:
                m3 = b
                m4 = d
            else:
                m3 = d
                m4 = b
        elif b > a and b > d:
            m2 = b
            if a > d:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
        else:
            m2 = d
            if a > b:
                m3 = a
                m4 = b
            else:
                m3 = b
                m4 = a
    if d > a and d > b and d > c:
        m1 = d
        if a > b and a > c:
            m2 = a
            if b > c:
                m3 = b
                m4 = c
            else:
                m3 = c
                m4 = b
        elif c > b and c > a:
            m2 = c
            if b > a:
                m3 = b
                m4 = a
            else:
                m3 = a
                m4 = b
        else:
            m2 = b
            if a > c:
                m3 = a
                m4 = c
            else:
                m3 = c
                m4 = a
    print(f"Números ordem recebidos: {a}, {b}, {c} e {d}")
    print(f"Números ordem crescente: {m4}, {m3}, {m2} e {m1}")
    print(f"Números ordem decrescente: {m1}, {m2}, {m3} e {m4}")
    