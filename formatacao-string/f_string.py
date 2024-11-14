#f-string uma das maneira de formatar string da maneira que desejar

# para utilizar deve-se adicionar um "f" antes das aspas de uma declaração de string

# minha_string = f"Olá mundo {expr}"

# dentro das chaves podemos passar expressões como variaveis, métodos, chamar funções entre outros

# alguns exemplos

nome = "vinicius"

minha_string = f"Olá" + nome + "."
minha_string1 = f"Olá {nome}"
minha_string2 = f"Olá {nome.upper()}"
minha_string3 = f"Quantos anos você tem? {10+9}"
minha_string4 = f"Numero 2 é maior que 1? {2>1}"
minha_string5 = f"Numero dois está na lista [4,6,7]? {2 in [4,6,7]}"

print(minha_string)
print(minha_string1)
print(minha_string2)
print(minha_string3)
print(minha_string4)
print(minha_string5)


##############################################3

from datetime import datetime

frutas = ['Maça', 'Uva', 'Laranja']

for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} | Número de letras: {len(fruta): 3}"
    print(minha_fruta)

print()

pi = 3.1415
meu_numero = f"O numero de PI é: {pi:.1f}"
meu_numero_deslocado = f"O numero PI deslocado é: {pi:6.1f}"
meu_numero_preciso = f"O numero PI mais preciso é {pi:.4f}"

print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()

minha_data = f"A data de hoje é {data}"
minha_data_formatada = f"A data de hoje é {data:%d/%m/%y}"

print(minha_data)
print(minha_data_formatada)