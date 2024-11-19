# operação de remover um arquivo, que está disponível por meio da função remove do módulo os do Python.

# sintaxe:
    # os.remove(caminho)

# Para remover diretório, devemos utilizar outra função, rmdir.

import os

with open("tratamento-excecao\\teste.txt", "w") as arquivo:
    print("Arquivo aberto")

try:
    os.remove("tratamento-excecao\\teste.txt")
    print("Arquivo removido")

except FileNotFoundError as erro:
    print("Arquivo não encontrado")
    print("Descrição: ", erro)

except PermissionError as erro:
    print("Não tem permissão")
    print("Descrição: ", erro)

except IsADirectoryError as erro:
    print("Remove serve apenas para arquivos")
    print("Descrição: ", erro) 



