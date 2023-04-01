import json

# Abre o arquivo JSON com os dados de faturamento
with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

# Inicializa as variáveis
menor = float('inf')
maior = float('-inf')
soma = 0
dias_acima_media = 0

# Percorre os valores de faturamento e atualiza as variáveis
for valor in faturamento.values():
    if valor == 0: # Ignora dias sem faturamento
        continue
    elif valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor
    soma += valor

