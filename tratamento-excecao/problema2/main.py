import os
from criar_diretorios import criar_diretorios
from mover_arquivos import mover_arquivos

def main():
       diretorio_trabalho = "tratamento-excecao\\problema2\\diretorio_trabalho"
       diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                     os.path.join(diretorio_trabalho, 'txt'),
                     os.path.join(diretorio_trabalho, 'jpg')]
 
       # Criar diretórios se não existirem
       criar_diretorios(diretorios)
 
       # Mover arquivos para os diretórios correspondentes
       mover_arquivos(diretorio_trabalho)
 
if __name__ == "__main__":
       main()