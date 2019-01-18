peso = float(input("Informe o peso: "))

excesso = peso - 50

print("Peso informado: ",peso)
if excesso <= 0:
    print("Peso dentro do padrão máximo estipulado! ")
else:
    print("Sua multa é de R$: ",excesso*4)
