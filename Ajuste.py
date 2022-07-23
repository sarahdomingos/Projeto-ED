# from MenuPrincipal import tente_novamente
from utils import checkMatriculaExiste, resgatarDisciplinasAtivas, resgatarDadosDisciplinas

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
    else:
        
        for i in range(0, len(disciplinas)):
            disciplinas[i] = resgatarDadosDisciplinas(disciplinas[i])


        print(f'Aluno: {matriculaValida[2]}')
        print(f'Número de matrícula: {matricula}\n')

        print("Disciplinas:\n")
        print("___________________________________________________________________________________________")
        print("|          Disciplina          |       Carga Horária          |          Horários          |")
        print("|_____________________________________________________________|____________________________|")

        for i in disciplinas:
            
            print(f'|          {i["nome"]}       |            {i["carga horária"]}                |                            |')
            print("|_____________________________________________________________|____________________________|")

                



















    
