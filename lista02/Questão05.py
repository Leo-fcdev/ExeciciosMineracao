"""
A minha sobrinha está aprendendo as letras do alfabeto. Ela ainda confunde o que é vogal e consoante. Você topou fazer comigo um programa que verifica se uma letra é vogal ou consoante. Então, é isso, né? Vamos lá? 
"""

letra = input("Qual é sua letra? ")

if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print(f"A letra '{letra}' é uma vogal")
else:
    print(f"A letra '{letra}' é uma consoante")