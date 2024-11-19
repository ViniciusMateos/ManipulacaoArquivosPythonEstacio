# podemos listar os documentos dentro de um diretório com a função scandir do módulo OS

# sintexe:
    # os.scandir(caminho)

import os

try:
    entrada = os.scandir("tratamento-excecao\\manipulacao-diretorios") # escaneia um arquivo

    for docs in entrada: # escaneando cada arquivo dentro do diretório
        print("Nome: ", docs.name) # retorna o nome do arquivo ou dir
        print("Caminho: ", docs.path) # retorna o caminho do arquivo ou dir
        print("É diretório?", docs.is_dir()) # verifica se é dir
        print("É arquivo?", docs.is_file()) # verifica se é arquivo
        print("Tamanho: ", docs.stat().st_size, "B") # função stat pode retornar alguns atributos relacionado ao arquivo ou dir, nesse caso é o tamanho

except FileNotFoundError as erro:
    print("Diretório não encontrado")
    print("Descrição: ", erro)

except NotADirectoryError as erro:
    print("Caminho não é um diretório")
    print("Descrição: ", erro)