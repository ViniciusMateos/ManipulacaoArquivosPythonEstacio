arquivo = open("lendo-conteudo\\teste.txt")

conteudo = arquivo.readline()

print("Tipo de conteúdo:", type(conteudo))

print("Conteúdo retornado pelo readline:")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado pelo readline:")
print(repr(proximo_conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado pelo readline:")
print(repr(proximo_conteudo)) #função interna repr para mostrar o conteúdo real contido da variável conteúdo

arquivo.close()

# a cada chamada do "arquivo.readline()" ele lê a próxima linha