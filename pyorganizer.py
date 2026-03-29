import sys
import os
import pathlib

# Cria as configurações
class Config:
    def __init__(self):
        self.working_folder = "Documents"
        self.final_folder = "Documents"
        self.recursive_organization = False 

# Cabeçalho universal dos menus
def header():
    print("============================")
    print("\tPYORGANIZER")
    print("============================")

def procurar(pasta):
    # Procurar a pasta
    path = pathlib.Path().home()
    
    folders_list = [x for x in path.rglob(pasta)]

    if len(folders_list) == 0:
        clear()
        print("Não foi encontrado esse diretório.")
        return
    elif (len(folders_list) > 1) and (folders_list[0].isdir() == False):
        clear()
        print("Há mais de um diretório com esse nome.")
        return
    
    return folders_list[0]
    
    

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

# Cria o objeto organizador
class Organizer:
    def __init__(self):

        #Obtém as configurações
        self.config = Config()
        
        #Inicializa
        self.inicializar()
        
    # Função para dar início ao script
    def inicializar(self):
        
        # Mantém o menu para ver o que o usuário deseja fazer
        menu()
        while True:
            # Pega a resposta
            answer = str(input()).lower()

            # Escolhe a função escolhida pela pessoa
            if answer == "x":
                # Limpa a tela e sai
                clear()
                sys.exit("Programa Finalizado!")
            elif answer == "1":
                ...
            elif answer == "2":
                # Inicia o menu de modificação
                clear()
                self.modificar()
            else:
                print("Opção Inválida, digite novamente: ",end="")

    # Função para modificar as configurações
    def modificar(self):
        
        # Mantém o menu para ver o que o usuário deseja fazer
        
        while True:
            menu_modificacao(self.config)
            # Pega a resposta digitada
            answer = str(input()).lower()

            # Escolhe a função escolhida pela pessoa
            if answer == "x":
                # Lista o menu inicial novamente
                clear()
                menu()
                return
            elif answer == "1":
                # Obtém a pasta alvo
                print("Digite o nome da pasta que deseja: ",end="")
                answer = str(input())
                found = procurar(answer)

                # Caso encontre, altera as configurações
                if  found:
                    self.config.working_folder = found.name
                    print("Alterado!")
                    return
                
            elif answer == "2":
                # Obtém a pasta alvo
                print("Digite o nome da pasta que deseja: ",end="")
                answer = str(input())
                found = procurar(answer)

                # Caso encontre, altera as configurações
                if  found:
                    self.config.final_folder = found.name
                    print("Alterado!")
                    self.inicializar()
                    
            elif answer == "3":
                is_activated = self.config.recursive_organization
                while True:
                    if is_activated:
                        print("Deseja desativar o modo recursivo? [Y/N]: ",end="")
                        answer = str(input()).lower().strip()
                        if answer == "y":
                            self.config.recursive_organization = False
                            print("Desativado!")
                            break
                        elif answer == "n":
                            
                            break
                        else: 
                            print("Opção inválida!")
                    else:   
                        print("Deseja ativar o modo recursivo? [Y/N] ",end="")
                       
                        if answer == "y":
                            self.config.recursive_organization = True
                            print("Ativado!")
                            break
                        elif answer == "n":
                            break
                        else: 
                            print("Opção inválida!")
Organizer()
