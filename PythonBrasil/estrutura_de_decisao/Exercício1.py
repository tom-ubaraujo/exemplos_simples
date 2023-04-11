num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

if num1 > num2:
    print("O primeiro número, %i é maior!" %num1)
    #outra forma de imprimir
    print("O primeiro número, {} é maior!".format(num1))
else:
    print("O segundo número, %i é maior!" %num2)
    #outra forma de imprimir
    print("O primeiro número, {} é maior!".format(num2))