"""
Você agora quer fazer um programa apenas para exercitar a sua lógica. Basicamente, você viu que o IBGE faz uma consulta de 5 preços para ver a média de preços. Você resolveu fazer o seguinte: ler os valores, calcular a média e verificar quais valores estão acima da média. 
"""
preco = []

for i in range(5):
    valor = float(input(f"Qual o valor do produto {i+1}: "))
    preco.append(valor)

media = sum(preco) / len(preco)

print(f"A media desse produto é de: R$ {media}")
print(f"Produtos acima da media de preço:")
for i in range(5):
    if (preco[i] > media):
        print(f"O produto {i+1} {preco[i]:.2f} está acima da media")
