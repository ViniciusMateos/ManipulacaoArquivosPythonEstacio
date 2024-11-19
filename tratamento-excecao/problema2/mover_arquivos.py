import os
import shutil

# funcao para mover arquivos

def mover_arquivos(diretorio_origem):
       for arquivo in os.listdir(diretorio_origem):
           caminho_arquivo = os.path.join(diretorio_origem, arquivo)
           if os.path.isfile(caminho_arquivo):
               extensao = arquivo.split('.')[-1].lower()
               if extensao in ['pdf', 'txt', 'jpg']:
                   diretorio_destino = os.path.join(diretorio_origem, extensao)
                   try:
                       shutil.move(caminho_arquivo, diretorio_destino)
                       print(f"{arquivo} movido para {diretorio_destino}.")
                   except PermissionError:
                       print(f"Sem permissão para mover {arquivo}.")
                   except Exception as e:
                       print(f"Erro inesperado ao mover {arquivo}: {e}")
               else:
                   print(f"Extensão {extensao} de {arquivo} não é suportada.")