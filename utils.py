import os
import pathlib
import sys
import argparse

# Função para limpar tela
def clear():
    # Limpa a tela independente dp sistema
    os.system("cls" if os.name == "nt" else "clear")

# Cria as configurações
class Config:
    def __init__(self):
        self.working_folder = "Documents"
        self.final_folder = "Default"
        self.recursive_organization = False 

class Menu():
    def __init__(self, organizer):
        self.page = "Main"
        self.organizer = organizer
        self.config = organizer.config
    def main(self):
        print_menu()

        while True:
            clear()
            print_menu()
            # Pega a resposta
            answer = input().lower()

            # Escolhe a função escolhida pela pessoa
            if answer == "x":
                # Limpa a tela e sai
                clear()
                sys.exit("Programa Finalizado!")

            elif answer == "1":
                clear()
                self.organizer.organize()
            elif answer == "2":
                    # Inicia o menu de modificação
                clear()
                self.modificar()
            else:
                print("Opção Inválida, digite novamente: ",end="")

    def modificar(self):
        self.page = "Modify"
        # Mantém o menu para ver o que o usuário deseja fazer
        while True:
            print_menu(self.config)
            # Pega a resposta digitada
            answer = input().lower()

            # Escolhe a função escolhida pela pessoa
            if answer == "x":
                # Lista o menu inicial novamente
                clear()
                
                return
            elif answer == "1":
                # Obtém a pasta alvo

                answer = input("Digite o nome da pasta que deseja: ")
                found = get_folder(answer)

                # Caso encontre, altera as configurações
                if  found:
                    self.config.working_folder = found.name
                    clear()
                    print("Alterado!")
                    
                    return
                
            elif answer == "2":
                # Obtém a pasta alvo
                
                answer = input("Digite o nome da pasta que deseja: ")
                found = get_folder(answer)

                # Caso encontre, altera as configurações
                if  found:
                    self.config.final_folder = found.name
                    clear()
                    print("Alterado!")
                    
                    return

            elif answer == "3":
                # Envia o menu
                
                # Pega a recursividade e Checa se Já está ativado
                is_activated = self.config.recursive_organization
                # Se estiver
                if is_activated:

                    # Pergunta para o usuário
                    answer = input("Deseja desativar o modo recursivo? [Y/N]: ").lower().strip()

                    # Confere a resposta
                    if answer == "y":
                        # Altera as configurações
                        self.config.recursive_organization = False
                        clear()
                        print("Desativado!")
                        
                    elif answer == "n":
                        pass
                    else: 
                        print("Opção inválida!")
                else:   
                    # Pergunta para o usuário
                    answer = input("Deseja ativar o modo recursivo? [Y/N] ").lower().strip()

                    # Confere a resposta
                    if answer == "y":
                        # Altera as configurações
                        clear()
                        self.config.recursive_organization = True
                        print("Ativado!")

                        
                    elif answer == "n":
                        pass
                    else: 
                        print("Opção inválida!")


# Cabeçalho universal dos menus
def header():
    print("============================")
    print("\tPYORGANIZER")
    print("============================")

# Função para imprimir o menu inicial
def print_menu(config=None):
    header()
    if config:
        print(f"\n1. Modificar Pasta a Ser Organizada: {config.working_folder}\n2. Modificar Pasta Final: {config.final_folder}\n3. Organização recursiva: {config.recursive_organization}\nX. Voltar\n\n: ",end="")
    else:
        print("\n1. Iniciar\n2. Modificar Configurações\nX. Sair\n\n: ",end="")

# Função para pegar todas as pastas com determinado nome
def get_all_folders(name):
    # Escolhe o caminho inicial
    path = pathlib.Path().home()
    folders_list = []

    for archive in path.rglob(name):
        if archive.is_dir():
            folders_list.append(archive)
    
    return folders_list


def folder_exists(folder, arg):
    folders_list = get_all_folders(folder)
    
    # Pega o tamanho da lista
    list_length = len(folders_list)

    # Se não tiver pastas
    if list_length == 0:
        clear()
        sys.exit(arg, "Não foi encontrado um diretório com esse nome.")
        return False
    
    # Se tiver mais que uma pasta
    elif  list_length > 1:
        clear()
        sys.exit(arg, "Há mais de um diretório com esse nome.")

    return folder


def get_folder(name):
    # Pega as pastas com determinado nome
    folders_list = get_all_folders(name)
    
    # Pega o tamanho da lista
    list_length = len(folders_list)

    # Se não tiver pastas
    if list_length == 0:
        clear()
        print("Não foi encontrado esse diretório.")
        return
    
    # Se tiver mais que uma pasta
    elif  list_length > 1:
        clear()
        print("Há mais de um diretório com esse nome.")
        return

    # Se tiver só uma pasta, pega e retorna
    folder = folders_list[0]
    
    return folder
    
def get_ext_folder(pasta,ext):
    archives_list = [x for x in pasta.glob(ext)]
    
    if len(archives_list) == 0:
        archive = pathlib.Path(f"{pasta}/{ext}")
        archive.mkdir()
        return archive
    
    for archive in pasta.glob(ext):
        if archive.is_dir():
            return archive
        


def get_args():
    parser = argparse.ArgumentParser("Pyorganizer", description="A simple command-line program that enables you to easily organize your files into categories based on their extensions.")
    parser.add_argument("-d","--directory")
    parser.add_argument("-f","--finalfolder")
    parser.add_argument("-r","--recursive", action="store_true")
    args = parser.parse_args()

    return args

# Função para imprimir o menu de modificação
def organize_archive(archive, f_folder):
    # Pega o nome da pasta baseado na extensão
    extension = f"{archive.suffix.upper()}s".replace(".","")

    # Checa se a pasta já existe
    folder = get_ext_folder(f_folder, extension)

    archive.rename(folder / archive.name)

