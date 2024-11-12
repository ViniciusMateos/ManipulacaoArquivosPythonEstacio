# utilizamos o laço for para iterar diretamente sobre a variável arquivo.
# cada iteração, recebemos uma nova linha do arquivo, disponibilizada na variável linha

arquivo = open("lendo-conteudo\\teste.txt")

for linha in arquivo:
    print(repr(linha))

arquivo.close()
