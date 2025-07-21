# vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicita uma string ao usuário
texto = input("Digite uma string: ")

# Solicita um número inteiro ao usuário, com validação
while True:
    entrada = input("Digite um número inteiro (maior ou igual a zero): ")
    try:
        numero = int(entrada)
        if numero < 0:
            print("Erro: o número deve ser maior ou igual a zero.")
            continue
        break
    except ValueError:
        print("Erro: entrada inválida. Digite um número inteiro válido.")

# Cria a repetição da string separada por traços
resultado = "-".join([texto] * numero)

# Exibe o resultado da repetição
print("Resultado da repetição:", resultado)
