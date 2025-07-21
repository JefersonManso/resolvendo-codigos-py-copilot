# Solicita as três notas do usuário
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcula a média usando operadores aritméticos
    media = (nota1 + nota2 + nota3) / 3

    # Exibe a média formatada com duas casas decimais
    print(f"Média das notas: {media:.2f}")

except ValueError:
    print("Entrada inválida. Digite apenas números.")
