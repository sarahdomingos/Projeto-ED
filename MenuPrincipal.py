from utils import prioridadesMatricula, confirmar
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

pedidosMatricula = {21117369: 0, 21115821: 0, 19113291: 3, 21117122: 2}
# Esta função representa o menu inicial exibido para o usuário
def menu_Principal(inicio):
    while True:
        print("############################################################\n")
        print("                 Menu do Sistema do Estudante\n")
        print("As opções disponíveis são:\n")
        print("1 - Fazer matrícula (apenas para calouros)")
        print("2 - Fazer matrícula (veteranos)")
        print("3 - Ajuste")
        print("4 - Reajuste\n")

        print("############################################################\n")
        print("                 Menu do Sistema do Coordenador\n")
        print("As opções disponíveis são:\n")
        print("10 - Finalizar período de MATRÍCULA")
        print("20 - Finalizar período de AJUSTE")
        print("30 - Finalizar período de REAJUSTE\n")

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
                matricula = Matricula.matricular_calouros("iniciar")
                prioridade = prioridadesMatricula(matricula)
                pedidosMatricula[matricula] = prioridade

            if opcaoConvert == 2:
                from Matricula_veterano import inicio   
                matricula = inicio()
                prioridade = prioridadesMatricula(matricula)
                pedidosMatricula[matricula] = prioridade
            
            if opcaoConvert == 3:
                import Ajuste
                Ajuste.ajustar("iniciar")

            if opcaoConvert == 4:
                import Reajuste
                Reajuste.reajustar("iniciar")
            
            if opcaoConvert == 10:
                listaOrdenada = confirmar(pedidosMatricula)
                print(f'\nLista final com a ordem de prioridade dos lunos:\n{listaOrdenada}\n')
        
menu_Principal('iniciar')
