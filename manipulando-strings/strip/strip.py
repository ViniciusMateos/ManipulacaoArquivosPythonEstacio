# quando é lido um texto ele vem com "\n" que as vezes pode ser considerado como lixo
# para remover isso na hora de exibiir é usado o método "strip()"

with open("manipulando-strings\\strip\\teste.txt") as arquivo:
        for linhas in arquivo:
            print(repr(linhas))

print("\n Exibindo com strip")

with open("manipulando-strings\\strip\\teste.txt") as arquivo:
      for linhas in arquivo:
            linhas_strip = linhas.strip()
            print(repr(linhas_strip))


#####################################################################

# Contando o real número de linhas
# Quando não usado o strip ele contabiliza também esses espaçõs em brancos de "\n" então para realmente saber o tanto de linhas com escritas é necessário usar o strip

print("\nExibindo quantidade sem strip")

with open("manipulando-strings\\strip\\teste.txt") as arquivo:
    contador = 0
    for linhas in arquivo:
        if linhas:
            contador += 1

    print("Quantidade de linhas:", contador)


print("\nExibindo quantidade com strip")

with open("manipulando-strings\\strip\\teste.txt") as arquivo:
    contador = 0
    for linhas in arquivo:
        linhas_strip = linhas.strip()
        if linhas_strip:
            contador += 1

    print("Quantidade de linhas:", contador)