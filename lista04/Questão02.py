"""
Além de calcular a média dos salários, você resolve entender como os valores variam em relação a média. Desta forma, você deve calcular a variância para todos os valores da lista de salários em relação a média do conjunto. 
"""
qdt_registros = int(input("Digite a quantidade de registros que serão feitos: "))

salarios = []
for i in range(1, qdt_registros + 1):
    valor = float(input("Digite o salário: "))
    salarios.append(valor)

media = sum(salarios) / len(salarios)
  
variancia = sum((salario - media) ** 2 for salario in salarios) / len(salarios)

print(f"A variancia dos valores é de: {variancia:.2f}")
