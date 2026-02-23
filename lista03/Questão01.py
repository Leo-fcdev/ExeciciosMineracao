"""
Quando crianças aprendemos as tabuadas dos números 2, 3, 4, assim em diante. Vamos criar a tabuada do número que quisermos. O usuário deve informar o número que ele deseja a tabuada e você deve imprimir a tabuada tal como abaixo:

Número da tabula: 5
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

"""

multiplicando = int(input("Digite o número que será multiplicado: "))

print(f"Tabuada do {multiplicando}:")
for x in range(0, 10):
    multiplicado = x + 1
    produto = multiplicando * multiplicado
    print(f"{multiplicando} x {multiplicado} =  {produto}" )
     