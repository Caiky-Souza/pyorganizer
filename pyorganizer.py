import sys
from utils import *


# Cria o objeto organizador
class Organizer:
    def __init__(self):
        #Obtém as configurações
        self.config = Config()
        
        #Inicializa
        self.setup()
        
    # Função para dar início ao script
    def setup(self):
        # Pega os argumentos recebidos no programa
        args = get_args()

        # Se não forem fornecidos argumentos, inicia o menu interativo
        if not args.directory and not args.finalfolder:
            menu = Menu(self)
            menu.main()
            

        # Se o usuário forneceu um diretório
        elif args.directory:  
            # Pega e confere se a pasta a ser organizada existe
            folder = folder_exists(args.directory, arg="Working Directory:")
            # Guarda a pasta final nas configurações
            self.config.working_folder = folder

            # Se o usuário forneceu pasta de destino 
            if args.finalfolder:
                # Checa se ela existe
                final_folder = folder_exists(args.finalfolder, arg="Final Directory:")
                # Salva a pasta nas configurações
                self.config.final_folder = final_folder
            
            # Se o usuário solicitou uma organização recursiva
            if args.recursive:
                # Salva nas configurações
                self.config.recursive_organization = True

            self.organize()
        # Se o usuário forneceu apenas outro campo
        else:
            sys.exit("Por favor, forneça o nome de um diretório utilizando -d.")

    # Função para iniciar o processo de organização
    def organize(self):
        # Receber a pasta inicial
        w_folder = get_folder(self.config.working_folder)
        
        # receber a pasta final
        f_folder = self.config.final_folder
        
        # Checar se a pasta final é a padrão
        if f_folder == "Default":
            f_folder = w_folder
        else:
            f_folder = get_folder(f_folder)

        # Saber se quer recursivo
        recursive = self.config.recursive_organization

        # Ver se essas pastas existem
        if w_folder and f_folder:
            # Trabalha cada arquivo
            if recursive:
                for archive in w_folder.rglob("*"):
                    if archive.is_dir():
                        continue
                    organize_archive(archive, f_folder)
            else:
                for archive in w_folder.glob("*"):
                    
                    if archive.is_dir():
                        continue

                    organize_archive(archive, f_folder)

            sys.exit("Concluído")

def main():
    Organizer()                     


main()
