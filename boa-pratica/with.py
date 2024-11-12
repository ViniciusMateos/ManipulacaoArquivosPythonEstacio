# palavra reservada "with" garante que o arquivo seja fechado corretamente sem ter que chamar o método close ao final

# sintaxe
    # with open(caminho, modo) as nome: (seu código indentado)

with open("boa-pratica\\teste.txt", "r") as arquivo:

    for linhas in arquivo:
        print(linhas)

with open("boa-pratica\\teste.txt", "a") as arquivo:
        
    arquivo.write("Adicionando usando o with para fechar adequadamente")


with open("boa-pratica\\teste.txt", "r") as arquivo:
    for linhas in arquivo:
        print(linhas)
