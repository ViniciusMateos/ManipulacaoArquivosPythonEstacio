arquivo_escrita = open("escrevendo-conteudo\\teste.txt", "w") #necessário passar o segundo parâmetro "w" dizedno o modo que queremos operar - no modo "w" ele irá apagar o conteudo do arquivo e começará a escrever.

arquivo_escrita.write("Conteúdo escrito") # escrevendo no arquivo
arquivo_escrita.write("\nConteúdo escrito na segunda linha") # escrevendo no arquivo

arquivo_escrita.close()

reabrir_arquivo = open("escrevendo-conteudo\\teste.txt") #reabir no modo de leitura para conseguir ler

conteudo_escrito = reabrir_arquivo.readlines()

print(repr(conteudo_escrito))

reabrir_arquivo.close()

##############################

arquivo_escrita2 = open("escrevendo-conteudo\\teste.txt", "a") # modo append tambem podendo ser usado para escrito que irá adicionar o conteudo

conteudo = ["\nEscrevendo conteudo com lista", "\nSegunda linha escrita com lista"]

arquivo_escrita2.writelines(conteudo)

arquivo_escrita2.close()

reabrir_arquivo2 = open("escrevendo-conteudo\\teste.txt")

conteudo_escrito2 = reabrir_arquivo2.readlines()

print(repr(conteudo_escrito2))