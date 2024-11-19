import os
from SobrescreverCabecalho import processar_arquivo

def main():
       diretorio_trabalho = "diretorio_trabalho"
       arquivo_origem = "tratamento-excecao\\problema\\diretorio_trabalho\\arquivo_origem.txt"
       arquivo_destino = "tratamento-excecao\\problema\\diretorio_trabalho\\arquivo_destino.txt"
 
       processar_arquivo(arquivo_origem, arquivo_destino)
 
if __name__ == "__main__":
    main()