# MÉTODOS DE STRINGS - Python

# Métodos básicos
texto = "aprendo muito com a lila!"

# Obter tamanho da String
tamanho_texto = len(texto)  # 25

# Colocar a primeira letra maiúscula
primeira_maiuscula = texto.capitalize()  # "Aprendo muito com a lila!"

# Colocar todos os caracteres em maiúsculo
texto_maiusculo = texto.upper()  # "APRENDO MUITO COM A LILA!"

# Colocar todos os caracteres em minúsculo
texto_minusculo = texto.lower()  # "aprendo muito com a lila!"

# Remoção de espaços
texto = " vou salvar esse post pra consultar "

# Remover espaço no início (esquerda)
texto_lstrip = texto.lstrip()  # "vou salvar esse post pra consultar "

# Remover espaço no final (direita)
texto_rstrip = texto.rstrip()  # " vou salvar esse post pra consultar"

# Remover espaço no início e no final
texto_strip = texto.strip()  # "vou salvar esse post pra consultar"

# Busca e manipulação
texto = "não gosto de café"

# Encontra o índice da primeira ocorrência do elemento
posicao_cafe = texto.find("café")  # 13

# Encontra o índice da última ocorrência do elemento
posicao_letra_e = texto.rfind("e")  # 17

# Fatiar uma String [início:final:passo]
pedaco_texto = texto[10:12]  # "de"

# Substituir elemento por outro
texto_alterado = texto.replace("não", "eu")  # "eu gosto de café"

# Separar a String em um array de substrings
substrings = texto.split(" ")  # ["não", "gosto", "de", "café"]

# Juntar um array de String em uma única String
novo_texto = " ".join(substrings)  # "não gosto de café"

# Verificação e validação
texto = "bazzingatxt"

# Testa se todos os caracteres são letras
so_letra = texto.isalpha()  # False

# Testa se todos os caracteres são números
so_numero = texto.isdigit()  # False

# Testa se todos os caracteres são alfanuméricos
so_alfanumerico = texto.isalnum()  # True

# Testa se todos os caracteres são maiúsculos
so_maiusculo = texto.isupper()  # False

# Testa se todos os caracteres são minúsculos
so_minusculo = texto.islower()  # True

# Testa se começa com substring
comeca_com = texto.startswith("Sheldon")  # False

# Testa se termina com substring
termina_com = texto.endswith("txt")  # True
