# Solicita a operação antes de tudo
operacoes_validas = ['+', '-', '*', '/']
operacao = input("Escolha a operação (+ - * /): ")

# Valida a operação
while operacao not in operacoes_validas:
    print("Operação inválida. Tente novamente.")
    operacao = input("Escolha a operação (+ - * /): ")

# Solicita os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Executa a operação
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = abs(numero1 - numero2)  # Subtração absoluta
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero."

# Exibe o resultado
print("Resultado:", resultado)
# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.


