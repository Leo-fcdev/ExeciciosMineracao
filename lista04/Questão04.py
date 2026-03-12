"""
Ordenar é uma das atividades mais frequentes que fazemos em vários problemas na computação. Nós podemos ordenar os nomes, ordenar os salários, ordenar as datas de nascimento. Faça um programa que leia os salários dos funcionários de uma empresa até que um valor zero seja informado. Após ler os salários, você deve ordená-los e obter o valor central da lista.
"""

salarios = []

valor = float(input("Digite o valor do salário (caso queira encerrar digite 0)"))
salarios.append(valor)

while valor != 0:
    valor = float(input("Digite o valor do salário (caso queira encerrar digite 0)"))
    if valor == 0:
        break
    
    salarios.append(valor)

salarios.sort()

print(f"Os salários ordenados são {salarios}")

qtd_salarios: float = len(salarios)

if qtd_salarios % 2 == 1:
    valor_central = salarios[qtd_salarios // 2]
else:
    valor_central = (salarios[qtd_salarios // 2 - 1] + salarios[qtd_salarios // 2]) / 2

print(f"O valor central dos salários é: {valor_central}")