import os
import pathlib

# Cria as configurações
class Config:
    def __init__(self):
        self.working_folder = "Documents"
        self.final_folder = "Default"
        self.recursive_organization = False 

# Cabeçalho universal dos menus
def header():
    print("============================")
    print("\tPYORGANIZER")
    print("============================")

def procurar(nome):
    # Procurar a pasta
    path = pathlib.Path().home()
    
    folders_list = [x for x in path.rglob(nome)]

    if len(folders_list) == 0:
        clear()
        print("Não foi encontrado esse diretório.")
        return
    elif (len(folders_list) > 1) and (folders_list[0].is_dir() == False):
        clear()
        print("Há mais de um diretório com esse nome.")
        return
    
    return folders_list[0]
    
def procurar_pasta_ext(pasta,ext):
    archives_list = [x for x in pasta.glob(ext)]
    
    if len(archives_list) == 0:
        path = pathlib.Path(f"{pasta}/{ext}")
        new_folder = path.mkdir()
        return path
    elif (len(archives_list) > 0) and (archives_list[0].is_dir()):
        return archives_list[0]
    print(archives_list)



# Função para imprimir o menu inicial
def menu():
    header()
    print("\n1. Iniciar\n2. Modificar Configurações\nX. Sair\n\n: ",end="")

# Função para imprimir o menu de modificação
def menu_modificacao(config):
    header()
    print(f"\n1. Modificar Pasta a Ser Organizada: {config.working_folder}\n2. Modificar Pasta Final: {config.final_folder}\n3. Organização recursiva: {config.recursive_organization}\nX. Voltar\n\n: ",end="")

# Função para limpar tela
def clear():
    # Limpa a tela independente dp sistema
    os.system("cls" if os.name == "nt" else "clear")