arquivo = open("lendo-conteudo\\teste.txt")

conteudo = arquivo.read()

print("Tipo de conteúdo:", type(conteudo))

print("Conteúdo retornado pelo read:")
print(repr(conteudo)) #função interna repr para mostrar o conteúdo real contido da variável conteúdo

arquivo.close()

# retorna todo o conteúdo junto 