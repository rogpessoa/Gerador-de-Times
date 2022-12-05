from random import shuffle
from BabaV3.interface import *


def criar_arquivo(arq):
    try:
        a = open(arq, 'w+')
        a.close()
    except:
        print("Não foi possível criar o arquivo")
    else:
        print(f"Arquivo {arq} criado com sucesso...")


def arquivo_existe(arq):
    try:
        a = open(arq, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def ler_arquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print("Erro ao abrir arquivo") #caso o erro seja ao abrir o arquivo
    else:
        cabecalho('JOGADORES CADASTRADOS')
        try:
            print(f"\033[31m{'Jogador':<30}{'Nivel':>3}\033[m")
            for v in a:
                dado = v.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f"{dado[0]:<30}{dado[1]:>3}")

        except: #se o arquivo for aberto e der erro ao apresentar os cadastrados
            print("Erro ao gravar as alterações")
    finally:
        a.close()


def sorteia(arq, *times): #funcao para sortear os times
    time1 = list()
    time2 = list()
    time3 = list()
    jogadores = list()
    try:
        a = open(arq, 'rt')
    except KeyboardInterrupt:
        print('\033[0;31mO usuário interrompeu o programa\033[m')

    except:
        print("Erro ao abrir arquivo")
    else:
        jogadores = [[dado for dado in dado.split(";")] for dado in a.readlines()]
        qtdtime = len(jogadores) / 6
        shuffle(jogadores)
        if qtdtime < 3:
            print(f"\033[32mNos temos {len(jogadores)} jogadores e podemos ter apenas dois times com 6 jogadores\033[m")
        elif qtdtime < 3:
            print(f"\033[32mNos temos {len(jogadores)} e podemos ter 3 times ou mais\033[m")
        for c, v in enumerate(jogadores): #sorteios dos times
                if v[1] not in time1: #adiiconar jogadores ao time 1
                    time1.append(v[0])
                    c += 1
                if c >= 6:
                    break
        for c, v in enumerate(jogadores): #adicionar jogadores ao time 2
            if v[1] not in time2 and v[0] not in time1:
                time2.append(v[0])
                c += 1
            if c >= 12:
                break
        if 13 < len(jogadores) < 18:
            print("\033[31mO terceiro time ficará com menos de 6 jogadores\033[m")
            for c, v in enumerate(jogadores): #adicionar jogdaores ao time 3 com menos de 6
                if v[1] not in time3 and v[0] not in time1 and v[0] not in time2:
                    time3.append(v[0])
                    c += 1
        else:
            for c, v in enumerate(jogadores): #adicionar jogdaores ao time 3 completo
                if v[1] not in time3 and v[0] not in time1 and v[0] not in time2:
                    time3.append(v[0])
                    c += 1
        print(time1)
        print(time2)
        print(time3)

    finally:
        a.close()

def cadastra(arq, nome="desconhecido", nivel="n1"):
    try:
        valida = nome.isalpha()
        if valida == True:
            a = open(arq, 'a')#append - adiciona novos usuarios ao arquivo
    except KeyboardInterrupt:
        print('O usuario interrompeu o programa')
        return 0
    except (ValueError, TypeError):
        print("Voce digitou algo errado, revise e tente novamente!")

    else:
        try:
            a.write(f"{nome};{nivel}\n")
        except KeyboardInterrupt:
            print("O usuário interrompeu o programa")
            return 0
        except:
            print("Ocorreu um erro na hora de cadastrar o novo jogador")
        else:
            print(f"O cadastro de {nome} foi realizado com sucesso...")
            a.close()

#Modulo de exclusao de jogadores##########################################################
def excluir_jogador(arq, nome): #funcao para excluir jogador da lista
    lista_atualizada = [] #lista para receber os dados tratados
    try: #Esse bloco vai ler o arquivo e excluir da lista criada|| o segundo with vai atualizar o arq
        with open('cadastrobaba.csv', 'r') as arquivo_exclusao:
            linhas = arquivo_exclusao.readlines()
            for linha in linhas:
                dado = linha.replace('\n', '')
                dados = dado.split(';')
                lista_atualizada.append(dados)
            for index, item in enumerate(lista_atualizada):
                if nome in item[0]:
                    print(f'O jogador escolhido para exclusão foi: {nome}')
                    lista_atualizada.pop(index)



#Bloco que vai pegar a lista ja modificada e atualizar no arquivo csv
        with open('cadastrobaba.csv', 'w') as muda_arquivo:
            for jogador, nivel in enumerate(lista_atualizada):
                muda_arquivo.write(f'{nivel[0]};{nivel[1]}\n')

            print("Arquivo atualizado com sucesso...")

    except:
        print("Erro ao tentar abrir arquivo")
#
# #MODULO DE EXCLUIR FUNCIONANDO, FALTANDO APENAS DEIXAR NOME E NIVEL NA MESMA LINHA
# #TENTAR TRANSFORMAR EM LISTA E EXCLUIR O INDEX PELA LISTA