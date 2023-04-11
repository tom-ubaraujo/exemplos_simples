a = float(input("Informe o preço do 1º produto: "))
b = float(input("Informe o preço do 2º produto: "))
c = float(input("Informe o preço do 3º produto: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print("O produto mais barato é: ",menor)
