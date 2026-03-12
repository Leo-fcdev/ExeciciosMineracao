"""
Você está desenvolvendo um sistema para analisar dados de um conjunto de funcionários de uma empresa. Você está fazendo a Análise Exploratória de Dados (AED) e percebeu que não tem um código para calcular a média dos salário da base. Faça um programa que receba o número de registros a serem lidos e leia os salários. Você deve calcular a média dos salários lidos e exibir apenas os salários acima da média. 
"""

qdt_registros = int(input("Digite a quantidade de registros que serão feitos: "))

salarios = []
for i in range(1, qdt_registros + 1):
    valor = float(input("Digite o salário: "))
    salarios.append(valor)

media = sum(salarios) / len(salarios)

print(f"A media salárial é de: {media:.2f}")

for salario in salarios:
    if( salario > media):
        print(f"O salário acima da média é: {salario:.2f}")
