def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Por favor digite um numero inteiro valido\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[0;31mO usuario interrompeu o programa!\033[m")
            return 0
        else:
            return n

def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    try:
        print(linha())
        print(txt.center(42)) #vai pegar o texto do programa principal e jogar aqui
        print(linha())
    except KeyboardInterrupt:
        print("O usuario interrompeu o programa")
        return 0


def menu(lista): #cria a funcao menu
    cabecalho("MENU PRINCIPAL") #chama a funcao cabecalho dentro do menu
    c = 1 #contador para criar opcao do menu
    for item in lista: #for para percorrer a lista
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m") #A variavel c mostra o contador o item o nome do menu
        c += 1
    print(linha()) #funcao linha para imprmir apos o menu
    opc = leia_int("\033[32mSua Opção: \033[m") #Aguarda o usuario digitar
    return opc
