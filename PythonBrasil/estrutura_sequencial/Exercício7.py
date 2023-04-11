valor_hora = float(input("Informe o valor recebido por hora: "))
qtd_horas = float(input("Informe a quantidade de horas trabalhadas: "))

bruto = valor_hora * qtd_horas

inss = (bruto/100)*8
ir = (bruto/100)*11
sind = (bruto/100)*5

liquido = bruto - inss - ir - sind

print("+ Salário Bruto : R$ ",bruto)
print("- IR (11%) : R$ ",ir)
print("- INSS (8%) : R$ ",inss)
print("- Sindicato ( 5%) : R$ ",sind)
print("= Salário Líquido : R$ ",liquido)