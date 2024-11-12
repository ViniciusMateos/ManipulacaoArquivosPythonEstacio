# Desenvolver um programa em Python que execute as seguintes operações:

# Carregar uma imagem simples do sistema de arquivos.
# Converter a imagem em uma representação binária usando a biblioteca PIL (Python Imaging Library).
# Exibir os dados binários da imagem.
# Salvar esses dados em um arquivo binário.
# Fazer uma cópia desse arquivo binário.
# Manipular os dados do arquivo binário cópia (por exemplo, inverter os bytes, adicionar ruído etc.).
# Carregar a imagem modificada a partir do arquivo binário e exibi-la para ver o efeito das manipulações.

from PIL import Image
import numpy as np
 
def main():
    # Carregar a imagem original
    img = Image.open("manipulando-dados-binarios\simple-icon.jpeg")
    img.show()
 
    # Converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()
 
    # Salvar os dados binários em um arquivo
    with open("manipulando-dados-binarios\original_img.bin", "wb") as file:
        file.write(binary_data)
 
    # Copiar o arquivo binário
    with open("manipulando-dados-binarios\original_img.bin", "rb") as original_file:
        data = original_file.read()
    
    with open("manipulando-dados-binarios\copy_img.bin", "wb") as copy_file:
        copy_file.write(data)
 
    # Manipulação dos dados do arquivo binário cópia
    # Exemplo: Inverter os bytes
    with open("manipulando-dados-binarios\copy_img.bin", "rb") as file:
        data = bytearray(file.read())
    
    # Inverte todos os bytes
    data = data[::-1]
 
    with open("manipulando-dados-binarios\copy_img.bin", "wb") as file:
        file.write(data)
 
    # Carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()
 
if __name__ == "__main__":
    main()