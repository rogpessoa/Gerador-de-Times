from BabaV3.funcoes import *
from BabaV3.interface import *
from time import sleep

#########Inicio do programa#########################################
arq = "cadastrobaba.csv"
if not arquivo_existe(arq): #Verifica se existe o arquivo csv. Caso nao exista ele cria
    criar_arquivo(arq)

while True:
    resposta = menu(["Jogadores Cadastrados", "Adicionar Jogador", "Sortear times", "Excluir Jogador", "Sair do Programa"])
    if resposta == 1: #Mostra os jogadores ja cadastrados no sistema
        ler_arquivo(arq)
    if resposta == 2:#Cadastrar novos jogadores
        cabecalho("CADASTRAR NOVO JOGADOR")
        nome = str(input("Digite o nome do jogador "))
        nivel = str(input("Digite o nivel do jogador (N1,N2,N3) "))
        cadastra(arq, nome, nivel)
    if resposta == 3: #Sorteia os times
        cabecalho("SORTEIO DOS TIMES")
        sorteia(arq)
        cabecalho("Times sorteados!")
        break
    if resposta == 4: #Exclui jogadores da lista
        cabecalho("EXCLUSÃO DE JOGADORES")
        nome = str(input("Digite o nome do jogador que deseja excluir "))
        excluir_jogador(arq, nome)
    if resposta == 5: #Finaliza o programa
        cabecalho("\033[31mFinalizando Programa...\033[m".center(50))
        sleep(0.5)
        cabecalho("Volte sempre!")
        break
