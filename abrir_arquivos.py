# Neste comentário está a forma simples de fazer:
# arq_txt = open("arquivo.txt","w")

nome = input("Informe seu nume: ")
idade = input("Informe sua idade: ")
cidade = input("Informe sua cidade: ")

arq_nome = "arquivo.txt"
arq_abertura = 'r'
arq_txt = open(arq_nome,arq_abertura)

arq_txt.write(nome + '\n' + idade + '\n' + cidade)

arq_txt.close()

arq2 = open("arquivo.txt","r")
print(arq2.read())
