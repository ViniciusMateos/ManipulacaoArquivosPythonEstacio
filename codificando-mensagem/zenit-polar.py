# codificação ZENIT POLAR é um tipo de cifra de substituição simples na qual as letras de duas palavras ou grupos de letras são usadas para substituir uma pela outra.
# cada letra em "ZENIT" é substituída pela letra correspondente em "POLAR" e vice-versa
# bidirecional e simétrica, a mesma substituição é usada para codificar e decodificar mensagens.

# **Z** é substituída por **P** e **P** por **Z**.
# **E** é substituída por **O** e **O** por **E**.
# **N** é substituída por **L** e **L** por **N**.
# **I** é substituída por **A** e **A** por **I**.
# **T** é substituída por **R** e **R** por **T**.

# as outras letras que não estão incluídas na cifra são deixadas inalteradas

def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    trocas = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for velha, nova in trocas:
        text = text.replace(velha, nova)
    return text
 
def main():
    # Entrada da frase e aplicação da codificação
    frase = "A raposa marrom rápida pula por cima do cachorro preguiçoso"
    frase = frase.title()  # Primeira letra de cada palavra em maiúscula
 
    # Dividir a frase em palavras
    palavras = frase.split()
 
    # Processar cada palavra na lista usando ZENIT POLAR
    palavras_codificadas = [zenit_polar_replace(palavra) for palavra in palavras]
 
    # Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(palavras_codificadas)
    print("Original:", frase)
    print("Codificada:", palavras_codificadas)
 
if __name__ == "__main__":
    main()