import sys
from utils import *


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
                clear()
                self.iniciar()
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
                    clear()
                    print("Alterado!")
                    menu()
                    return
                
            elif answer == "2":
                # Obtém a pasta alvo
                print("Digite o nome da pasta que deseja: ",end="")
                answer = str(input())
                found = procurar(answer)

                # Caso encontre, altera as configurações
                if  found:
                    self.config.final_folder = found.name
                    clear()
                    print("Alterado!")
                    menu()
                    return

            elif answer == "3":
                # Envia o menu
                
                # Pega a recursividade e Checa se Já está ativado
                is_activated = self.config.recursive_organization
                # Se estiver
                if is_activated:

                    # Pergunta para o usuário
                    print("Deseja desativar o modo recursivo? [Y/N]: ",end="")
                    answer = str(input()).lower().strip()

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
                    print("Deseja ativar o modo recursivo? [Y/N] ",end="")
                    answer = str(input()).lower().strip()

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
    def iniciar(self):
        # Receber a pasta inicial
        w_folder = procurar(self.config.working_folder)
        
        # receber a pasta final
        f_folder = self.config.final_folder
        
        # Checar se a pasta final é a padrão
        if f_folder == "Default":
            f_folder = w_folder
        else:
            f_folder = procurar(f_folder)

        # Saber se quer recursivo
        recursive = self.config.recursive_organization

        # Ver se essas pastas existem
        if w_folder and f_folder:
            # Trabalha cada arquivo
            if recursive:
                for archive in w_folder.rglob("*"):
                    if archive.is_dir():
                        continue
                    # Checa a extensão do arquivo
                    extension = f"{archive.suffix.upper()}s".replace(".","")
                    # Checa se a extensão já tem pasta
                    folder = procurar_pasta_ext(f_folder, extension)

                    archive.rename(folder / archive.name)
            else:
                for archive in w_folder.glob("*"):
                    if archive.is_dir():
                        continue
                    # Checa a extensão do arquivo

                    extension = f"{archive.suffix.upper()}s".replace(".","")

                    # Checa se a extensão já tem pasta
                    folder = procurar_pasta_ext(f_folder, extension)

                    archive.rename(folder / archive.name)
    
            print("Concluído!")
            sys.exit()
                        
Organizer()
