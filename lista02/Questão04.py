"""
Um baralho contém 52 cartas de 4 tipos (naipes) diferentes: paus, espadas, copas e ouro. Em cada naipe, que consiste de 13 cartas, 3 dessas cartas contêm as figuras do rei, da dama e do valete, respectivamente. Faça um programa que leia um número de 1 a 13 e informe qual carta o número representa por extenso. Lembrando que temos algumas cartas especiais: 1 (Ás), 11 (Valete), 12 (Rainha), 13 (Rei). 
"""
numero = int(input("Qual é o número da sua carta? "))

if(numero == 1):
    print("Sua carta é o Ás")
elif(numero == 2):
    print("Sua carta é um dois")
elif(numero == 3):
    print("Sua carta é um três")
elif(numero == 4):
    print("Sua carta é um quatro")
elif(numero == 5):
    print("Sua carta é um cinto")
elif(numero == 6):
    print("Sua carta é um seis")
elif(numero == 7):
    print("Sua carta é um sete")
elif(numero == 8):
    print("Sua carta é um oito")
elif(numero == 9):
    print("Sua carta é um nove")
elif(numero == 10):
    print("Sua carta é um dez")
elif(numero == 11):
    print("Sua carta é um valete")
elif(numero == 12):
    print("Sua carta é uma rainha")
elif(numero == 13):
    print("Sua carta é um rei")
else:
    print("O número slecionado não existe no baralho")