#Python disponibiliza a função interna chamada open

#   arquivo = open(caminho)

#Utilizamos a função open com o parâmetro caminho
#parâmetro é uma string que representa a localização do arquivo no sistema de arquivos.

arquivo = open("operacoes-basicas\\teste.txt")


#############################################################################################

#funções para exibir os caminhos absolutos e relativos de um arquivo ou diretório

# a função path.relpath para imprimir o caminho relativo
# a função path.abspath para exibir o caminho absoluto 

# para ter acesso a esses métodos é necessário importar "os"

import os

print(os.path.relpath("teste.txt")) # relativo

print(os.path.abspath("teste.txt")) # absoluto

#############################################################################################

# Imprimir variável arquivo

print(arquivo)

# tipo do objeto, TextIOWrapper, que trata de arquivos de texto
# nome do arquivo, name='dados.txt'
# modo de acesso ao arquivo, mode='r'.
# codificação do arquivo, encoding='cp1252