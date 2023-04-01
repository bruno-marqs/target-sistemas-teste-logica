num = int(input("Digite um número: "))

# Inicializa as variáveis de Fibonacci
a, b = 0, 1

# Percorre a sequência de Fibonacci até encontrar um número maior ou igual a 'num'
while b < num:
    a, b = b, a+b

# Verifica se 'num' pertence à sequência de Fibonacci
if b == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
