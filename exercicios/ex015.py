km = float(input("Quantos km foram rodados: "))
dias =  int (input("Por quantos dias o carro foi alugado: "))
f = (60 * dias) + (0.15 * km)
print(f"O total a ser pago é R$ {f:.2f}")
