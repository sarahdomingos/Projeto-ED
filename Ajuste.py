# from MenuPrincipal import tente_novamente
from utils import checkMatriculaExiste
from openpyxl import load_workbook
import os 

def ajustar(inicio):

    matriculaValida = False 
    matricula = [0]

    while (not matriculaValida):
        matricula = int(input('Digite o seu número de matrícula:\n>'))
        matriculaValida = checkMatriculaExiste(matricula)[0]

        if (matriculaValida == False):
            print("Número de matrícula inválido.\nPor favor tente novamente.")      

        # Mostrar qual matérias o aluno está cursando e perguntar se ele deseja trancar 
        
        index = matricula[1]


    
