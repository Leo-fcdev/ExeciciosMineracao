"""
Em um supermercado é comum que no caixa os produtos sejam passados até que finalize-se a compra. Você deve fazer um programa que leia os preços dos produtos, até que o preço zero seja informado. O total da compra deve ser informado no final. Você deve, basicamente, somar todos os preços informados.
"""
valorProduto = float(input("Qual o valor do produto? "))
soma = 0

while (valorProduto != 0):
    soma += valorProduto
    valorProduto = float(input("Qual o valor do produto? "))

print(f"A Conta final deu: R${soma:.2f} ")