"""
Toda vez que um casal descobre que vai ter uma filha/um filho, definir o nome da criança é uma das tarefas mais desafiadoras. Apesar de querermos nomes únicos, o mais comum é que o nome das crianças se repitam. Definir a frequência de cada nome é uma atividade que o IBGE realiza  para definir quais são os nomes masculinos e femininos mais frequentes no Brasil. Você está avaliando uma base de dados de pacientes de um hospital. Nessa questão, você vai ler a quantidade total de paciente e os nomes deles. Depois disso, informe a quantidade de ocorrências de cada nome
"""

qtd_pacientes = int(input("Qual a quantidade de pacientes? "))

nomes_masculinos = []
nomes_femininos = []

resultado = input("O nome do qual a pesquisa deve ser feita é Masculino ou Feminino?")

if resultado == "Masculino":
    for i in range(1, qtd_pacientes + 1):
        nomes = input("Digite um nome: ")
        nomes_masculinos.append(nomes)
        nomes_contagem = nomes_masculinos

elif resultado == "Feminino":
      for i in range(1, qtd_pacientes + 1):
        nomes = input("Digite um nome: ")
        nomes_femininos.append(nomes)
        nomes_contagem = nomes_femininos

frequecia = {}

for nome in nomes_contagem:
    if nome in frequecia:
        frequecia[nome] += 1
    else:
        frequecia[nome] = 1

print(f"\nFrequência dos nomes ({resultado})")
for nome, contagem in frequecia.items():
    print(f"{nome}: {contagem} ocorrência(s)")

