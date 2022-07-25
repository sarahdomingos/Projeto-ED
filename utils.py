# Aqui ficam funções utilitárias para os outros arquivos 
import os
from openpyxl import load_workbook

def checkMatriculaExiste(numero):

    numeroExiste = False
    nome = None
    
    file = os.getcwd() + '\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb['Página1']

    for index in range(1, len(page['C'])):
        if (page['C'][index].value == numero):
            numeroExiste = True
            break
    
    if (numeroExiste == False):
        index = -1 


    return [numeroExiste, index, page['A'][index].value]

def resgatarDisciplinasAtivas(index):

    file = os.getcwd() + '\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb['Página1']

    materias = page['H'][index].value

    if (materias != None):
        materias = materias.split(', ')
    else:
        materias = []

    return materias

def removerDisciplina(codigoDisciplina, index):
    file = os.getcwd() + '\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb["Página1"]

    disciplinas = page['H'][index].value
    disciplinas = disciplinas.split(", ")

    print('Tamanho', len(disciplinas))

    for i in range(0, len(disciplinas)):
        print(disciplinas[i] == codigoDisciplina)
        if (disciplinas[i] == codigoDisciplina):
            disciplinas.pop(i)
    
    print(', '.join(disciplinas))

    page['H'][index].value = ', '.join(disciplinas)

    try: 
        wb.save("dados_dos_alunos.xlsx")
        return True 
    except:
        return False 

def resgatarDadosDisciplinas(codigo):

    file = os.getcwd() + '\Disciplinas - Trabalho Estrutura de Dados.xlsx'
    wb = load_workbook(file)
    page = wb['Obrigatórias CC']    

    disciplina = {}

    found = False

    for index in range(1, len(page['A'])):
        if (page['A'][index].value == codigo):
            disciplina = {
                "codigo": page['A'][index].value,
                "nome": page['B'][index].value,
                "periodo": page['D'][index].value,
                "dias": page['F'][index].value,
                "carga horária": page['E'][index].value,
                "horario": page['G'][index].value
            }
            break
        
    if (not found):
        page = wb['Eletivas CC']

        for index in range(1, len(page['A'])):
            if (page['A'][index].value == codigo):
                disciplina = {
                    "codigo": page['A'][index].value,
                    "nome": page['B'][index].value,
                    "carga horária": page['D'][index].value,
                    "dias": page['E'][index].value, 
                    "horario": page['F'][index].value
                }
                break 

    return disciplina

def resgatarMateriasPagas(index):
    file = os.getcwd() + '\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb['Página1']

    materias = page['F'][index].value

    if (materias != None):
        materias = materias.split(', ')
    else:
        materias = []

    return materias


def resgatarMateriasPossiveisAjuste(materiasPagas): 
    
    file = os.getcwd() + '\Disciplinas - Trabalho Estrutura de Dados.xlsx'
    wb = load_workbook(file)

    disciplinas = []

    page = wb["Obrigatórias CC"]
    for index in range(1, len(page['A'])):
        # print(page['C'][index].value)
        # checa se a disciplina tem pre-requisitos
        if (page['C'][index].value == 0):
            disciplinas.append({
                "codigo": page['A'][index].value,
                "nome": page['B'][index].value,
                "carga horária": page['D'][index].value,
                "dias": page['E'][index].value,
                "horarios": page['F'][index].value
            })
        else:
            if (page['C'][index].value != None):
                prereq = page['C'][index].value

                # Separa os pre-requisitos em um array
                prereq = prereq.split(",")
                print(prereq)
                possivelPagar = True

                for prerequisito in prereq:
                    print(prerequisito)
                    if (prerequisito not in materiasPagas):
                        possivelPagar = False 

                if (possivelPagar == True and page['A'][index].value not in materiasPagas):
                    disciplinas.append({
                        "codigo": page['A'][index].value,
                        "nome": page['B'][index].value,
                        "carga horária": page['D'][index].value,
                        "dias": page['E'][index].value,
                        "horarios": page['F'][index].value
                    })

    page = wb["Eletivas CC"]
    for index in range(1, len(page['A'])):
        if (page['C'][index].value == 0):
            disciplinas.append({
                "codigo": page['A'][index].value,
                "nome": page['B'][index].value,
                "carga horária": page['D'][index].value,
                "dias": page['E'][index].value,
                "horarios": page['F'][index].value
            })
        else:
            if (page['C'][index].value != None):
                prereq = page['C'][index].value
                prereq = prereq.split(",")
                
                possivelPagar = True

                for prerequisito in prereq:
                    if (prerequisito not in materiasPagas):
                        possivelPagar = False 
                
                if (possivelPagar == True and page['A'][index].value not in materiasPagas):
                    disciplinas.append({
                        "codigo": page['A'][index].value,
                        "nome": page['B'][index].value,
                        "carga horária": page['D'][index].value,
                        "dias": page['E'][index].value,
                        "horarios": page['F'][index].value
                    })

    return disciplinas
    #     else:
    #         # recupera os pre-requisitos da matéria

    #         prereq = page['C'][index].value
    #         print(prereq)
    #         prereq = prereq.split(", ")

    #         # checa 

    #         for prerequisito in prereq:
    #             if (prerequisito in materiasPagas):
    #                 disciplinas.append({
    #                     "codigo": page['A'][index].value,
    #                     "nome": page['B'][index].value,
    #                     "carga horária": page['D'][index].value,
    #                     "dias": page['E'][index].value,
    #                     "horarios": page['F'][index].value
    #                 })

    # page = wb["Eletivas CC"]
    # for index in range(1, len(page['A'])):
    #     # checa se a disciplina tem pre-requisitos
    #     if (page['C'][index].value == 0):
    #         disciplinas.append({
    #             "codigo": page['A'][index].value,
    #             "nome": page['B'][index].value,
    #             "carga horária": page['D'][index].value,
    #             "dias": page['E'][index].value,
    #             "horarios": page['F'][index].value
    #         })
    #     else:
    #         # recupera os pre-requisitos da matéria

    #         prereq = page['C'][index].value
    #         prereq = prereq.split(", ")

    #         # checa 

    #         for prerequisito in prereq:
    #             if (prerequisito in materiasPagas):
    #                 disciplinas.append({
    #                     "codigo": page['A'][index].value,
    #                     "nome": page['B'][index].value,
    #                     "carga horária": page['D'][index].value,
    #                     "dias": page['E'][index].value,
    #                     "horarios": page['F'][index].value
    #                 })


    
        











