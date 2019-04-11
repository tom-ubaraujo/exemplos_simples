niveis = ['fácil','médio','difícil']

tentativas = [3,2,1]

frase_velkoz = "Vel'Koz: O __0__ de __1__ humano permanece __2__. Será que pararam de __3__?"
frase_lissandra = "Lissandra: O __0__ adormecerá sua __1__. Isto não __2__ de uma __3__, eu já venci a __4__."
frase_thresh = "Thresh: __0__ não lhe trará __1__ de bom, mas é __2__ para os meus __3__. Existe __4__, existe \
__5__, e então... existe a mim!"

resp_velkoz = ["ponto","fusão","inconsistente","evoluir"]
resp_lissandra = ["frio","dor","passa","batalha","guerra"]
resp_thresh = ["gritar","nada","música","ouvidos","vida","morte"]

lista_frases = [frase_velkoz,frase_lissandra,frase_thresh]
lista_respostas = [resp_velkoz, resp_lissandra, resp_thresh]

def nivel_dificuldade():
    """
     Exibe mensagem de início de jogo; Define o nível de dificuldade do jogo, escolhido pelo jogador;
     O jogador deve informar o nível dentre as opções: fácil/médio/difícil, caso contrário o jogo não se inicia.
    """
    print("Olá invocador, neste jogo, você deverá completar frases de campeões de League of Legends!")
    print("Mostre seu conhecimento sobre os campos da justiça!")
    
    dificuldade = input("Escolha o nível: ('fácil' - 'médio' - 'dificil') ").lower()

    while dificuldade not in niveis:
        dificuldade = input("Escolha inválida! Escolha o nível: ('fácil' - 'médio' - 'dificil') ").lower()
    return niveis.index(dificuldade)

def monta_nivel():
    """
    Seleciona a frase, a quantidade de tentativas de acordo com a dificuldade e as respostas do nível escolhido.
    Retorna frase, resposta e quantidade de tentativas permitidas no nivel como argumentos, utilizados na função jogar() 
    """
    nivel = nivel_dificuldade()
    resposta_nivel = lista_respostas[nivel]
    frase_nivel = lista_frases[nivel]
    tentativas_nivel = tentativas[nivel]

    return resposta_nivel, frase_nivel, tentativas_nivel

def jogar():
    """
    Inicia o jogo no nivel escolhido, exibindo a frase do nível específico e controla as frases
    e respostas informadas pelo jogador, de acordo com a quantidade de chances de acerto para o nível escolhido.
    A cada tentativa é informada a quantidade de erros permitidos, equando o jogador termina a frase, é exibida
    mensagem de prabenização.
    Se o jogador perder, é exibida a mensagem de game over.
    """
    (resp,frase,tent) = monta_nivel()

    index = 0

    while (tent > -1) and (index < len(resp)):
        print("Tentativas restantes: ",tent)
        print(frase)
        palavra = input("Informe a palavra que complete o campo __{}__: ".format(index)).lower()

        if palavra == resp[index]:
            print("Resposta correta!")
            frase = frase.replace(('__'+str(index)+'__'),resp[index])
            index += 1
        else:
            print("Resposta errada! Tente novamente!")
            tent -= 1
    if tent > -1:
        print(frase)
        print("Parabéns invocador, você completou toda a frase!!!",)
    else:
        print("Todas as tentativas esgotadas! GAME OVER!")
    
jogar()




