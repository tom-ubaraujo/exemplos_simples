a = int(input("Informe 1º num: "))
b = int(input("Informe 2º num: "))
c = int(input("Informe 3º num: "))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

print("O maior número é: ",maior)
print("O menor número é: ",menor)