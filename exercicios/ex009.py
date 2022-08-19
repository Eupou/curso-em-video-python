from re import I


n = int(input("Digite um número para saber sua tabuada "))
i = 0
while i <= 10:
    res = n * i
    print(f'{n} x {i} = {res}')
    i += 1
