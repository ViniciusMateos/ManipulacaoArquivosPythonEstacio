arquivo = open("atributos-objeto-arquivo\\teste.txt")

#atributos
print("Nome do arquivo: ", arquivo.name) # caminho do arquivo
print("Modo do arquivo: ", arquivo.mode) # r, default
print("Arquivo está fechado?", arquivo.closed) #false

# método "close()" serve para fechar o arquivo
arquivo.close()

print("Arquivo está fechado?", arquivo.closed) # true