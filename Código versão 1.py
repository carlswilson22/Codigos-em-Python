# Calculadora Simples

num1 = float(input("Digite o primeiro número: "))
op = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if op == '+':
    print("Resultado:", num1 + num2)
elif op == '-':
    print("Resultado:", num1 - num2)
elif op == '*':
    print("Resultado:", num1 * num2)
elif op == '/':
    print("Resultado:", num1 / num2)
else:
    print("Operação inválida")
