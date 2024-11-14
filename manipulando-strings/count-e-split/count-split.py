# é possível contar quantas vezes determinada palavra aparece com o método count com a seguinte sintaxe

# contagem = variavel_string.count(palavra)

with open("manipulando-strings\\count-e-split\\teste.txt") as arquivo:
    conteudo = arquivo.read()
    contagem = conteudo.count("contagem")

    print("Número de vezes da palavra contagem = ", contagem)

# o método count ele leve em considereção o parâmetro sem separar por palavras
# Exemplo: na frase "amo comer amoras" e vocÊ quer saber quantas vezes a palavra "amo" apareceu, ele irá retornar duas vezes por também estar presente na palavra "amora"
# ai que o método split entra para separar as string em palavras
# a sintaxe é a seguinte, e o parâmetro será o que irá separar as string (se nao passar parametro será utilizado espaços como parametro)

# lista_termos = variavel_string.split(separador)

print("\nUtilizando split")

frase1 = "eu amo comer amoras"
lista_frase1 = frase1.split()
print(lista_frase1)

frase2 = "Amora abacaxi    vasco   da  gama"
lista_frase2 = frase2.split()
print(lista_frase2)

frase3 = "carro,moto,futebol"
lista_frase3 = frase3.split(",")# passando como parametro a "," que será o que separa as palavras
print(lista_frase3)


########################################################

print("\nResolvendo o problema da palavra amo")
print("\nSem split")

frase = "eu amo comer amoras"
contagem = frase.count("amo")
print("Quantidade de amo na frase = ", contagem)

print("\nCom split")

lista_palavras = frase.split()
contagem = lista_palavras.count("amo")
print("Quantidade de amo na frase = ", contagem)