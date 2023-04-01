# Input da String a ser invertida
original = input("Insira aqui a frase/palavra para inverter:\n")

# Lista com inversão dos caracteres
lista_inversa = []
for i in range(len(original) - 1, -1, -1):
    lista_inversa.append(original[i])


