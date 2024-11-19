# operação de renomear disponível no módulo OS também, serve para renomear arquivos

# sintaxe:
    # os.rename(origem, destino)

import os

with open("tratamento-excecao\\teste.txt", "w") as arquivo:
    print("Arquivo aberto")

try:
    os.rename("tratamento-excecao\\teste.txt", "tratamento-excecao\\testerenomeado.txt")
    print("Renomeado")

except FileNotFoundError as erro:
    print("Arquivo não encontrado")
    print("Descrição: ", erro)

except PermissionError as erro:
    print("Não tem permissão")
    print("Descrição: ", erro)

except FileExistsError as erro:
    print("Arquivo de destino já existe")
    print("Descrição: ", erro) 

# Para os casos em que desejamos renomear sobrescrevendo o arquivo destino, caso ele exista, podemos utilizar a função replace, também do módulo os.


