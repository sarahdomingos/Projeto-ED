# Aqui ficam funções utilitárias para os outros arquivos 
import os
from openpyxl import load_workbook

def checkMatriculaExiste(numero):

    numeroExiste = False
    
    file = os.getcwd() + '\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb['Página1']

    for i in range(1, len(page['C'])):
        print(page['C'][i].value)
        if (page['C'][i].value == numero):
            numeroExiste = True
            break
    
    if (numeroExiste == False):
        i = -1 

    return [numeroExiste, i]


def resgatarMateriasAtivas(index):

    file = os.getcwd() + '\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb['Página1']

    materias = page['H'][index]

    if (materias.value is not None):
        materias = materias.value.split(', ')
    else:
        materias = []
    
    # Buscar os dados da matéria
    if (len(materias) > 0):
        file = os.getcwd() + '\Disciplinas - Trabalho Estrutura de Dados.xlsx'
        wb = load_workbook(file)
        page = wb['Página1']






resgatarMateriasAtivas(116)


    
