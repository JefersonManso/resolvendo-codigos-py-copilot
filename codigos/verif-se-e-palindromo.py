# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e transforma em minúsculas para comparação segura
palavra_formatada = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra_formatada[::-1]

# Verifica se é um palíndromo
if palavra_formatada == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
