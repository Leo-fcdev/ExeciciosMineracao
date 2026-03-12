"""
Achar o valor mínimo e o máximo de uma lista é uma atividade recorrente. A gente quer achar o menor preço de um produto, o maior valor de venda. Mas, às vezes, a gente quer transformar os dados. Você deve fazer a leitura de dados numéricos até que um número negativo seja informado. Depois, você deve encontrar os valores mínimo e máximo. Uma vez que os encontrou, você deve realizar a seguinte transformação: 

novo_valor = ( valor - min ) / ( max - min ) 
"""

precos = []
valor = float(input("Digite o preço do produto (caso queira encerrar digite um valor negativo): "))


while valor >= 0:
    precos.append(valor)
    valor = float(input("Digite o preço do produto (caso queira encerrar digite um valor negativo): "))
    

min_preco = min(precos)
max_preco = max(precos)


for preco_atual in precos:
    novo_valor = (preco_atual - min_preco) / (max_preco - min_preco)

print(novo_valor)