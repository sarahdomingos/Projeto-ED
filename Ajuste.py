# from MenuPrincipal import tente_novamente
from utils import checkMatriculaExiste

def ajustar(inicio):

    matriculaValida = False 
    
    while (not matriculaValida):
        matricula = int(input('Digite o seu número de matrícula:\n>'))
        matriculaValida = checkMatriculaExiste(matricula)
        if (matriculaValida == False):
            print("Número de matrícula inválido.\nPor favor tente novamente.")      

    
