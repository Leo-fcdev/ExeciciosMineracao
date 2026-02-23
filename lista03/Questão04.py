"""
O zoom é uma plataforma de busca dos preços mais baixos da web para um mesmo produto. Ele além de mostrar o menor valor encontrado, apresenta também o preço médio do produto nos últimos trinta dias. Para encontrar o menor preço, o programa lê 6 preços durante o mês e encontra o menor deles. Você deve encontrar o menor preço do produto durante o mês. 
"""
soma = 0.0
media = 0.0
precos = []

for i in range(0, 6):
    valor = float(input("Digite um preço: "))
    precos.append(valor)

    soma += valor

media = soma / 6
menor_preco = min(precos)

print(f"O preço médio dos produtos é de R${media:.2f}")
print(f"O menor preço encontro foi R${menor_preco:.2f}")
