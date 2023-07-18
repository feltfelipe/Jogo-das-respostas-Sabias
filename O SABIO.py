import random  #biblioteca de randomização para as respostas
from time import sleep #função sleep da biblioteca time


def converte_em_lista(arquivo, lista): #função criada para ler o arquivo de texto com os ditos populares que serão usados para responder
    with open(arquivo, 'r', encoding='UTF8') as texto: #abrindo o arquivo e configurando para nossa linguagem (codificação)
        for linha in texto:
            lista.append(str(linha).replace('\n', '')) #loop para tratar (formatar) os dados e deixá-los pronto pro uso
        return lista

frases = [] #lista que vai receber os ditos populares

frases = converte_em_lista('ditados.txt', frases) #função criada acima sendo executada com o doc.txt e a lista como primeiro e segundo parâmetros.

# Inicio do programa principal
print('Olá, qual é o seu nome?')
sleep(1)
player = input('Seu nome: ') #variável para receber o nome do jogador
sleep(2)
print(f'Prazer em te conhecer {player}') #referência à variável
sleep(1)
print(f'Sou "O Sábio", me faça uma pergunta e te darei a resposta mais adequada!')
jogar = True #preparando o início do loop infinito
perguntas = [] #lista de perguntas
while jogar == True: #loop infinito para a interação do "jogador" enquanto 'jogar' for verdadeiro.
    print(f'Quer fazer uma pergunta {player}?')
    sleep(2)
    print('Sim (1)')
    print('Não (2)')
    try:
        resposta = int(input('Sua resposta: '))
        sleep(1)
        if resposta == 1: #se a resposta for sim, então:
            print('Ok, então faça sua pergunta')
            sleep(2)
            pergunta = input('Sua pergunta: ')
            if pergunta not in perguntas: #recebe a pergunta e e se não está na lista de perguntas já feitas, segue para fornecer a 'resposta sábia, rs'
                perguntas.append(pergunta)
                sleep(2)
                print('Hummm...')
                for i in range(5):
                    print('...')
                    sleep(1)
                resposta = frases[random.randint(0, len(frases))]
                print(resposta)
                sleep(5)
        elif resposta == 2: #caso o jogador não queira fazer a pergunta, jogar passa a ser falso e o programa é encerrado.
            jogar = False
            print(f'Ok, até a próxima {player}!')
    except:
        print('Resposta invalida, tente de novo!') #para os erros, retorna essa frase.
