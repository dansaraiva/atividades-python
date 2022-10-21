# Faça um programa que mostre as tabuadas dos números de 1 a 10
n: int
m: int
for n in range(1, 11):
    for m in range(0, 11):
        print(f"{n} x {m} = {m * n}")
    print()
