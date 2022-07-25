
# from Ajuste import ajustar
# from Reajuste import reajustar

# Esta função é chamada quando o usuário apresenta uma entrada inválida
def tente_novamente(inicio):
    print("------------------------------------------------\n")
    print("Gostaria de tentar novamente?\n")
    print("1 - Sim")
    print("2 - Não\n")

    opcao = input("Digite o número correspondente a sua resposta: ")

    # Aqui estamos dizendo que uma entrada vazia pode ser interpretada como um espaço vazio
    if opcao == '':
        opcao = ' '

    # Aqui estamos verificando se a entrada dada pelo usuário é um número inteiro
    try:
        int(opcao)
        verificacao_numero_inteiro = True

    except ValueError:
        verificacao_numero_inteiro = False

    # Se a entrada for um número inteiro, então...
    if verificacao_numero_inteiro == True:

        # Transformamos a entrada que estaa no formato de escrita em numeral
        opcaoConvert = int(opcao)

        # Se o usuário escolher a opção 1, então o mandamos de volta para o menu inicial
        if opcaoConvert == 1:
            menu_Principal('iniciar')

        # Se o usuário escolher a opção 2, então encerramos o programa
        if opcaoConvert == 2:
            print("------------------------------------------")
            print("Programa encerrado.")
            print("------------------------------------------")
            exit()

        # Se a entrada não for nem 1 e nem 2, então chamamos novamente a função de erro "tente_novamente"
        if opcaoConvert != 1 and opcaoConvert != 2:
            print("*********************************\n")
            print("Entrada Inválida!")
            print("Você só pode digitar 1 ou 2.")
            print("*********************************\n")

            tente_novamente('iniciar')

    # Se a entrada não for um número inteiro, então chamamos a função de erro 'tente_novamente'
    if verificacao_numero_inteiro == False:
        print("*********************************\n")
        print("Entrada Inválida!")
        print("Você só pode digitar 1 ou 2.\n")
        print("*********************************\n")

        tente_novamente('iniciar')


# Esta função representa o menu inicial exibido para o usuário
def menu_Principal(inicio):
    print("############################################################\n")
    print("                 Menu do Sistema do Estudante\n")
    print("As opções disponíveis são:\n")
    print("1 - Fazer matrícula (apenas para calouros)")
    print("2 - Fazer matrícula (veteranos)")
    print("3 - Ajuste")
    print("4 - Reajuste\n")

    opcao = input("Digite o número correspondente a sua escolha: ")

    # Aqui estamos verificando se a entrada dada pelo usuário é um número inteiro
    try:
        int(opcao)
        verificacao_numero_inteiro = True

    except ValueError:
        verificacao_numero_inteiro = False

    # Se a entrada não é um número inteiro, então chamamos a função de erro
    if verificacao_numero_inteiro == False:
        print("Entrada Inválida!")
        print("Você só pode digitar números inteiros enre 1 e 3.\n")
        tente_novamente("iniciar")

    # Se a entrada for um número inteiro, então...
    if verificacao_numero_inteiro == True:

        # Transformamos a entrada que está no formato de escrita em numeral
        opcaoConvert = int(opcao)

        if opcaoConvert == 1:
            import Matricula
            Matricula.matricular_calouros("iniciar")



menu_Principal('iniciar')
