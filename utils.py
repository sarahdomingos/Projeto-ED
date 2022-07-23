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

    materias = materias.split(', ')

    if (len(materias) == 0):
        return []
    
    return materias

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
