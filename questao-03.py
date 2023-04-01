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

# Calcula a média de faturamento mensal (considerando apenas os dias com faturamento)
media = soma / len([valor for valor in faturamento.values() if valor != 0])

# Conta o número de dias com faturamento superior à média
for valor in faturamento.values():
    if valor > media:
        dias_acima_media += 1

# Imprime os resultados
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
