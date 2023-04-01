# Faturamento por Estado
fat_sp = 67836.43
fat_rj = 36678.66
fat_mg = 29229.88
fat_es = 27165.48
fat_outros = 19849.53

# Faturamento total
fat_total = fat_sp + fat_rj + fat_mg + fat_es + fat_outros

# Percentual de cada Estado
percent_sp = (fat_sp / fat_total) * 100
percent_rj = (fat_rj / fat_total) * 100
percent_mg = (fat_mg / fat_total) * 100
percent_es = (fat_es / fat_total) * 100
percent_outros = (fat_outros / fat_total) * 100

# Imprimindo os resultados
print("Percentual de representação no faturamento total:\n")
print("Sao Paulo: ....... {:.2f}%".format(percent_sp))
print("Rio de Janeiro: .. {:.2f}%".format(percent_rj))
print("Minas Gerais: .... {:.2f}%".format(percent_mg))
print("Espirito Santos: . {:.2f}%".format(percent_es))
print("Outros Estados: .. {:.2f}%".format(percent_outros))