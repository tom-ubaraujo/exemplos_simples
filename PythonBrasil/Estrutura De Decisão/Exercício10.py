turno = input("Em qual turno estuda(M - V - N): ")

if turno.upper() == 'M':
    print("Bom dia!")
elif turno.upper() == 'V':
    print("Boa tarde!")
elif turno.upper() == 'N':
    print("Boa noite!")
else:
    print("Valor inválido!")