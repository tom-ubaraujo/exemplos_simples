altura = float(input("Informe a altura: "))
sexo = input("Informe seu sexo(M/F): ")

if sexo.capitalize() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7    

print("Seu peso ideal é: ",peso_ideal)