# Aqui ficam funções utilitárias para os outros arquivos 
import os
from openpyxl import load_workbook

def checkMatriculaExiste(numero):

    numeroExiste = False
    
    file = os.getcwd() + '\Projeto-ED\dados_dos_alunos.xlsx'
    wb = load_workbook(file)
    page = wb['Página1']

    for cell in page['C']:
        if (cell.value == numero):
            numeroExiste = True
            break
    
    return numeroExiste
