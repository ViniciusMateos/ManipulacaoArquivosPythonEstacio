arquivo = open("lendo-conteudo\\teste.txt")

conteudo = arquivo.readlines()

print("Tipo de conteúdo:", type(conteudo))

print("Conteúdo retornado pelo readlines:")
print(repr(conteudo)) #função interna repr para mostrar o conteúdo real contido da variável conteúdo 

arquivo.close()

#retorna uma lista onde cada lista é uma linha do arquivo