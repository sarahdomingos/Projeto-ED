# from MenuPrincipal import tente_novamente
from utils import adicionarDisciplinas, checarMateriaTemVagas, checkMatriculaExiste, resgatarDisciplinasAtivas, resgatarDadosDisciplinas, removerDisciplina, resgatarMateriasPagas, resgatarMateriasPossiveisAjuste
from tabulate import tabulate 

def ajustar(inicio):

    matriculaValida = [False, 0] 
    
    while (not matriculaValida[0]):
        matricula = int(input('\nDigite o seu número de matrícula:\n>'))
        matriculaValida = checkMatriculaExiste(matricula)
        if (matriculaValida[0] == False):
            print("Número de matrícula inválido.\nPor favor tente novamente.")      


    disciplinas = resgatarDisciplinasAtivas(matriculaValida[1])


    if (len(disciplinas) == 0):
        disciplinas = print('O aluno não está matriculado em nenhuma matéria no momento.')

        materiasPagas = resgatarMateriasPagas(matriculaValida[1])
        print(materiasPagas)
        disponiveis = resgatarMateriasPossiveisAjuste(materiasPagas)

        rows = [x.values() for x in disponiveis]
            
        newRows = []

        for element in rows:
            newRows.append(list(element))

        for i in range(0, len(newRows)):
            newRows[i].append(f"[{i+1}]")

        print(tabulate(newRows))




    # Caso o aluno esteja matriculado em alguma disciplina
    else:
        for i in range(0, len(disciplinas)):
            disciplinas[i] = resgatarDadosDisciplinas(disciplinas[i])

        rows = [x.values() for x in disciplinas]

        print(f'Aluno: {matriculaValida[2]}')
        print(f'Número de matrícula: {matricula}\n')

        print("Disciplinas atuais:\n")
        print(tabulate(rows, headers=["Código", "Nome", "Carga Horária", "Dias", "Horário"]))    
        
        print("Você deseja:\n")
        print("1 - Sair de uma das disciplinas")            
        print("2 - Se inscrever em uma disciplina diferente")   
        print("3 - Trocar uma disciplina por outra\n")

            
        escolha = input("Digite o número correspondente a sua escolha: ")
        valid = False

        # Checa se é número
        while (not valid):
            try:
                escolha = int(escolha)
                if (escolha == 1 or escolha == 2 or escolha == 3):
                    valid = True
                else:
                    print("Entrada inválida. Você só pode escolher entre 1 ou 2.")
                    escolha = input("Digite o número correspondente à sua escolha: ")
            except:
                print("Entrada inválida. Por favor digite um número.")
                valid = False
                escolha = input("Digite o número correspondente a sua escolha: ")

        if (escolha == 1):
            newRows = []

            for element in rows:
                newRows.append(list(element))

            for i in range(0, len(newRows)):
                newRows[i].append(f"[{i+1}]")

            print(tabulate(newRows))
            print("Selecione a disciplina da qual você deseja ser removido: ")
        
            disc = input("> ") 
        
            valid = False
            while (not valid):
                try:
                    disc = int(disc)
                    if (disc <= 0 or disc > len(newRows)):
                        print("Entrada inválida. Por favor escolher uma das opções disponíveis.")
                        disc = input("Digite o número correspondente à sua escolha: ")
                    else:
                        valid = True 
                except:
                    print("Entrada inválida. Por favor digite um número.")
                    valid = False
                    disc = input("Digite o número correspondente a sua escolha: ")

            materiaExcluida = newRows[disc-1]


            res = removerDisciplina(materiaExcluida[0], matriculaValida[1])
        
            if (res == True ):
                print(f'Você não está mais inscrito na disciplina {materiaExcluida[0]} - {materiaExcluida[1]}')
            else:
                print('Houve um na hora de persistir os dados')    

        elif (escolha == 2):
            materiasPagas = resgatarMateriasPagas(matriculaValida[1])
            materiasSolicitadas = resgatarDisciplinasAtivas(matriculaValida[1])
            rows = []
            disponiveis = resgatarMateriasPossiveisAjuste(materiasPagas, materiasSolicitadas)

            rows = [x.values() for x in disponiveis]
            
            newRows = []

            for element in rows:
                newRows.append(list(element))

            for i in range(0, len(newRows)):
                newRows[i].append(f"[{i+1}]")

            print(tabulate(newRows))

            print("Preencha aqui com os códigos das matérias nas quais você quer se inscrever da seguinte maneira:")
            print("Ex: COMP401")
            print("Ex: COMP401, COMP382")
            print("Sempre que houver mais de uma disciplina, separar por vírgulas:")

            disciplinasInscrever = str(input("> "))

            disciplinasInscrever = disciplinasInscrever.split(", ")

            for i in range(0, len(disciplinasInscrever)):
                if (not checarMateriaTemVagas(disciplinasInscrever[i])):
                    disciplinasInscrever.pop(i)
                    print(f'Não foi possível te matricular em {i}')
            
            for i in disciplinasInscrever:
                materiasSolicitadas.append(i)
            
            res = adicionarDisciplinas(materiasSolicitadas, matriculaValida[1])
            if (res):
                print("Ajuste feito.")
            else:
                print("Houve um erro na persistência dos dados.")  

        elif (escolha == 3):
            print("Aqui estão as matérias ")
            print(tabulate(rows))


ajustar('iniciar')
            

            





        






















    
