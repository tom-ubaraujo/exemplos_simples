area = float(input("Informe o tamanho da área a ser pintada: "))

litros = area / 6

latasG = litros / 18
latasP = litros / 3.6

print("Você pode comprar: ",latasG,"latas de 18 litros!")
print("Valor total a pagar: ", latasG * 80)
print("Você pode comprar: ",latasP,"latas de 3.6 litros!")
print("Valor total a pagar: ", latasP * 25)

# lata de 18 litros pinta 108 metros de área
# galão de 3.6 litros, pinta 21.6 metros de área