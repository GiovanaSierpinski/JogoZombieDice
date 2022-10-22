from random import shuffle, randint
#Giovana Sierpinski Pascoal da Silva - Analise e Desenvolvimento de Sistemas

#Classes
class Zumbi: #utilização dessa classe linha 72
    def __init__(self, nome, cerebros, tiros): #init é o construtor do objeto
        self.nome = nome #self é utilizado para indica referencia no próprio objeto
        self.cerebros = cerebros
        self.tiros = tiros

class Dado: #utilização dessa classe linhas 80-82
    def __init__(self, cor, lados, ladoSorteado):
        self.cor = cor
        self.lados = lados
        self.ladoSorteado = ladoSorteado

#Funções

def letra_acao(letra): #Utilização de dicionários para criar uma função parecida com o switch
    letras = { "C": "Cérebro - Você comeu um cérebro!", "P": "Passos - A vítima fugiu!", "T": "Tiro - Você levou um tiro!"}

    return letras.get(letra, "não foi estabelecido")

def joga_dado(listaDados):
    dado = listaDados.pop()
    numSorteado = randint(0, 5)
    dado.ladoSorteado = dado.lados[numSorteado]
    print("    ", dado.cor, ' ', letra_acao(dado.ladoSorteado))

    return dado

def Mostra_Lado(listaDadosJogados, jogadorAtual):
    for dado in listaDadosJogados:
        if (dado.ladoSorteado == "C"):
            jogadorAtual.cerebros = jogadorAtual.cerebros + 1
        elif (dado.ladoSorteado == "T"):
            jogadorAtual.tiros = jogadorAtual.tiros + 1

def imprimir_geral():
    print("╔═════ ∘◦ SCORE ◦∘ ══════╗")
    print("   Cérebros: ", jogadorAtual.cerebros)
    print("   Tiros: ", jogadorAtual.tiros)
    print("╚═══════ ∘◦ ❉ ◦∘ ═══════╝")

listaDadosJogados = []

def enfeite1():
    print("--------------------------------------------------------------------")

def enfeite2():
    print("˚꒷꒦︶︶︶︶︶꒷꒦︶︶˚꒷꒦︶︶︶︶︶꒷꒦︶︶˚꒷꒦︶︶︶︶︶꒷꒦︶︶˚꒷꒦︶︶︶︶︶꒷꒦︶︶")

#Introdução do Jogo
print("ZOMBIE DICE")

enfeite2()

nome = input("Por favor, digite seu nome: ")
print("Olá, seja bem-vindo ao Zombie Dice "+nome+"!")

numJogadores = int(input("Quantos zumbis irão jogar?"))

while numJogadores < 2:
    print("!!Para uma orda de zumbis, precisamos de mais que apenas 1!!")
    numJogadores = int(input("Informe um número maior de zumbis: "))

listaJogadores = []

for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')
    listaJogadores.append(Zumbi(nome, 0, 0))

#utilização de tuplas
lados_verde = ("C", "P", "C", "T", "P", "C")
lados_amarelo = ("T", "P", "C", "T", "P", "C")
lados_vermelho = ("T", "P", "T", "C", "P", "T")

dadoverde = Dado("Verde / ", lados_verde, "")
dadoamarelo = Dado("Amarelo / ", lados_amarelo, "")
dadovermelho = Dado("Vermelho / ", lados_vermelho, "")

listaDados = [
    dadoverde, dadoverde, dadoverde, dadoverde, dadoverde, dadoverde,
    dadoamarelo, dadoamarelo, dadoamarelo, dadoamarelo,
    dadovermelho, dadovermelho, dadovermelho
]

enfeite1()
print('Legal, vamos começar!!!')
enfeite2()

#Fim da introdução do Jogo

Ganhador = False


while (not Ganhador):
    for jogadorAtual in listaJogadores:
        print('É a vez do zumbi', jogadorAtual.nome )
        turno = True
        while(turno):
            shuffle(listaDados)#shuffle é utilizado para embaralhar uma sequencia
            numSorteado = randint(0, 5)

            d1 = joga_dado(listaDados)
            d2 = joga_dado(listaDados)
            d3 = joga_dado(listaDados)

            shuffle(listaDados) #shuffle é utilizado para embaralhar uma sequencia

            listaDadosJogados.clear()
            listaDadosJogados.append(d1)
            listaDadosJogados.append(d2)
            listaDadosJogados.append(d3)

            Mostra_Lado(listaDadosJogados, jogadorAtual)

            listaDados.append(d1)
            listaDados.append(d2)
            listaDados.append(d3)

            shuffle(listaDados)

            enfeite1()
            imprimir_geral()
            enfeite1()

            for zumbi in listaJogadores: #define perdedor
                if (zumbi.tiros >= 3):
                    print(' »» Ops, não foi dessa vez zumbi', zumbi.nome, ', você PERDEU!')
                    listaJogadores.remove(zumbi)

            for zumbi in listaJogadores: #define vencedor
                if (zumbi.cerebros >= 13):
                    print(' ☆ O ZUMBI', zumbi.nome, 'É O ZUMBI SUPREMO! VOCÊ GANHOU!')
                    Ganhador = True
                    turno = False
                    fimTurno = True
                    break
            

            if (len(listaJogadores) == 1):
                print(' ☆ O ZUMBI', listaJogadores[0].nome, 'É O ZUMBI SUPREMO! VOCÊ GANHOU!')
                Ganhador = True
                turno = False
                break

            fimTurno = False
            while(not fimTurno):
                fimTurno = True
                resposta = (input("Você deseja continuar jogando os dados, zumbi " + jogadorAtual.nome + "? (S/N) ")).lower()
                if resposta == "n":
                    print("Hora de passar a vez então!")
                    turno = False
                elif resposta == "s":
                    print("Então vamos continuar")
                else: 
                    fimTurno = False

enfeite1()
print("!FIM DE JOGO!")
enfeite2()
print("Obrigado por jogar Zombie Dice!")

#Fim do jogo