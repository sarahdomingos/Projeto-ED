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
                # "periodo": page['D'][index].value,
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
                    "dias": page['E'][index].value, 
                    "carga horária": page['D'][index].value,
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


def resgatarMateriasPossiveisAjuste(materiasPagas, materiasSolicitadas): 
    
    file = os.getcwd() + '\Disciplinas - Trabalho Estrutura de Dados.xlsx'
    wb = load_workbook(file)

    materiasDisponiveis = []

    page = wb["Obrigatórias CC"]

    obrigatorias_primeiro_quinto = []

    for i in range(1, len(page['A'])):

        if (page['D'][i].value != None and page['D'][i].value >= 1 and page['D'][i].value <= 5):
            obrigatorias_primeiro_quinto.append(page['A'][i].value)


    obrigatorias_possiveis = []
    eletivas_possiveis = []

    for i in range(1, len(page['A'])):
        if (page['A'][i].value != None) and page['A'][i].value not in materiasPagas and page['A'][i].value not in materiasSolicitadas:
            #split pre requisitos 
            prerequisitos = str(page['C'][i].value)
            prerequisitos = prerequisitos.split(",")
            
            if (page['C'][i].value == 'TODAS AS DISCIPLINAS OBRIGATÓRIAS DO 1º AO 5º PERÍODO'):
                obrigatorias_possiveis.append([page['A'][i].value, obrigatorias_primeiro_quinto])
            else:
                obrigatorias_possiveis.append([page['A'][i].value, prerequisitos])

    page = wb["Eletivas CC"]
    for i in range(1, len(page['A'])):
        if (page['A'][i].value != None) and page['A'][i].value not in materiasPagas and page['A'][i].value not in materiasSolicitadas:

            #split pre requisitos 
            prerequisitos = str(page['C'][i].value)
            prerequisitos = prerequisitos.split(",")

            if (page['C'][i].value == 'TODAS AS DISCIPLINAS OBRIGATÓRIAS DO 1º AO 5º PERÍODO'):
                eletivas_possiveis.append([page['A'][i].value, obrigatorias_primeiro_quinto])
            else:
                eletivas_possiveis.append([page['A'][i].value, prerequisitos])
    # 19218721

    for i in obrigatorias_possiveis:
        possivel = True 
        for valor in i[1]:
            if (valor not in materiasPagas and valor not in materiasSolicitadas):
                possivel = False
        if (possivel):
            materiasDisponiveis.append(i[0])

    for i in eletivas_possiveis:
        possivel = True 
        for valor in i[1]:
            if (valor not in materiasPagas and valor not in materiasSolicitadas):
                possivel = False
        
        if (possivel):
            materiasDisponiveis.append(i[0])
        

    for i in range(0, len(materiasDisponiveis)):
        materiasDisponiveis[i] = resgatarDadosDisciplinas(materiasDisponiveis[i])

    return materiasDisponiveis













