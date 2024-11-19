import os

# criar dirs caso nao tenha ainda

def criar_diretorios(diretorios):
       for diretorio in diretorios:
           if not os.path.exists(diretorio):
               try:
                   os.makedirs(diretorio)
                   print(f"Diretório {diretorio} criado.")
               except PermissionError:
                   print(f"Sem permissão para criar o diretório {diretorio}.")
               except Exception as e:
                   print(f"Erro inesperado ao criar {diretorio}: {e}")