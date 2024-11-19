# Quando abrimos um arquivo em modo leitura e esse arquivo não existe, o Python lança uma exceção do tipo FileNotFoundError
# Se não avisarmos ao Python o que fazer quando isso ocorrer, o programa será interrompido
# Nesse caso, um tratamento para essa exceção poderia ser: exibir um pop-up ao usuário informando que o arquivo não existe.

# Para tratar exceções, precisamos “envolver” o trecho de código passível de erro com a cláusula try/except ou try/except/finally. Veremos apenas a cláusula try/except.

# a sintaxe:

# try:
#     #codigo que pode gerar um exceção
# except Erro1 as erro:
#     # codigo alternativo caso erro 1
#     print(erro)

# except Erro2 as erro:
#     # codigo alternativo caso erro 2
#     print(erro)

# O código crítico que desejamos executar deve estar no escopo do try, enquanto o código alternativo, que será executado em caso de erro, deve estar no escopo do except.
# Uma mesma operação pode lançar mais de um tipo diferente de exceção, em que, para cada tipo, Erro1 e Erro2, devemos ter uma cláusula except específica.

print("Abrindo arquivo")

try:
    open("text.txt", "r")
    print("Arquivo aberto")

except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)

print("Término do programa")

# Um problema clássico que ocorre quando lidamos com arquivos é tentar alterar o conteúdo de um arquivo quando ele está aberto em outro programa. 
# No caso do sistema operacional Windows 10, é lançada uma exceção sobre permissão de acesso.

# criar mais um except para tratar o caso de não termos permissão para abrir um arquivo, mostrando o tratamento do problema levantado no parágrafo anterior.

print()

print("Abrindo arquivo sem permissão para alteração")

try:
    open("teste.txt")
    print("Arquivo aberto")

except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)

except PermissionError as erro:
    print("Não tem permissão para abrir o arquivo")
    print("Descrição: ", erro)

print("Término do programa")

