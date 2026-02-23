"""
As temperaturas no verão estão sendo cada vez mais quentes, assim como algumas regiões estão tendo invernos mais rigorosos. Devido a isso, alertas de emergências devem ser divulgados com antecedência. Você deve fazer um programa que leia as temperaturas máximas e mínimas durante uma semana. Você deve apresentar a mínima e a máxima da semana. 
"""
temperaturas = []

for i in range(0, 7):
    valor = int(input(f"Quantos graus fez no {i + 1}º dia: "))
    temperaturas.append(valor)

maior_temperatura = max(temperaturas)
menor_temperatura = min(temperaturas)

print(f"A maior temperatura registrada essa semana foi de {maior_temperatura} ºc")
print(f"A menor temperatura registrada essa semana foi de {menor_temperatura} ºc")