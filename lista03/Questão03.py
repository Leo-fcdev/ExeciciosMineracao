"""
A professora Alice precisa calcular a média das notas dos seus alunos. Os alunos possuem quatro notas bimestrais. A média final do aluno é a média aritmética das notas. Calcule e imprima a média de um aluno. 
"""
alunos = int(input("Qual a quantidade de alunos? "))
notas = 0.0
somaNotas = 0.0
media = 0.0

for i in range(0, alunos):
    for i in range(0, 4):
        notas = float(input(f"Qual a {i + 1}º nota? "))
        somaNotas += notas
        media = somaNotas / 4
    
    print(f"A média do aluno {i} é de: {media:.2f}")