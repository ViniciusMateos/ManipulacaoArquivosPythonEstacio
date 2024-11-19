#Para criar um diretório, utilizamos a função mkdir do módulo os, 
# enquanto, para remover um diretório, utilizamos a função rmdir, também do módulo os.

# sintaxe:
    # criar - os.mkdir(caminho)
    # remover os.rmdir(caminho)

# para remover um diretório ele precisa estar vazio

import os
import errno

try:
    os.mkdir("tratamento-excecao\\manipulacao-diretorios\\diretorioteste")
    print("Diretório criado")

    os.rmdir("tratamento-excecao\\manipulacao-diretorios\\diretorioteste")
    print("Diretório removido")

except PermissionError as erro:
    print("Não possui permissão para remover o diretório")
    print("Descrição: ", erro)

except FileExistsError as erro:
    print("Diretório já existe")
    print("Descrição: ", erro)

except FileNotFoundError as erro:
    print("Diretório não existe")
    print("Descrição: ", erro)

except OSError as erro: # caso o diretório esteja vazio
    print("Outro erro")
    print("O diretório está vazio?")
    print("Descrição", erro)

# Para os casos em que o diretório a ser removido não esteja vazio, será lançada a exceção OSError. 
# Essa exceção é mais abrangente.
# precisamos analisar mais o erro, principalmente o seu número, para verificar o que realmente aconteceu.

# O número do erro está disponível no atributo errno do objeto erro.
# códigos dos possíveis erros estão no módulo errno do Python e podem ser utilizados no tratamento das exceções para descobrir o que realmente deu errado.

# o numero do erro para diretório não vazio é 41

print()

os.mkdir("tratamento-excecao\\manipulacao-diretorios\\diretorioteste")
print("Criado diretório")

with open("tratamento-excecao\\manipulacao-diretorios\\diretorioteste\\teste.txt", "w") as arquivo:
    print("Criado arquivo dentro do diretório recém criado")

try:   
    os.rmdir("tratamento-excecao\\manipulacao-diretorios\\diretorioteste")

except OSError as erro:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY: # ou == 41 que é o valor do erro de dir não vazio
        print("Diretório não vazio")




