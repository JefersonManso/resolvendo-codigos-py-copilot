# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

# Solicita um número inteiro do usuário
try:
    numero = int(input("Digite um número inteiro: "))

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
