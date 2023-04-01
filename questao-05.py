# Input da String a ser invertida
original = input("Insira aqui a frase/palavra para inverter:\n")

# Lista com inversão dos caracteres
lista_inversa = []
for i in range(len(original) - 1, -1, -1):
    lista_inversa.append(original[i])

# Juntando os caracteres numa nova String
inversao = "".join(lista_inversa)

# Imprimindo o resultado
print(f"Frase/palavra invertida: {inversao}")
