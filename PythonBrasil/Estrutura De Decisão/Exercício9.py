"""
a = float(input("Informe o primeiro numero: "))
b = float(input("Informe o segundo numero: "))
c = float(input("Informe o terceiro numero: "))

if b < a and b < c:
    if a < c:
        print("Números: ",c,a,b)
    else:
        print("Números: ",a,c,b)
if c < a and c < b:
    if a < b:
        print("Números: ",b,a,c)
    else:
        print("Números: ",a,b,c)
if a < b and a < c:
    if b < c:
        print("Números: ",c,b,a)
    else:
        print("Números: ",b,c,a)
"""

lst = []
lst.append(float(input("Informe o primeiro numero: ")))
lst.append(float(input("Informe o segundo numero: ")))
lst.append(float(input("Informe o terceiro numero: ")))
lst.sort(reverse=True)
print(lst)