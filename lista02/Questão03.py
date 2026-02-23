"""
Em um jogo de tabuleiro, um jogador pode movimentar uma peça apenas se o número do seu dado for maior que o do seu adversário. Faça um programa que informe se o jogador pode ou não jogar aquela partida. Leia o número do dado do jogador e do seu adversário e informe quem deve jogar. No caso de empate, nenhum dos jogadores joga. 
"""
import random

print("Rolando dados...")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print(f"O dado do Jogador 1 caiu em {dado1}")
print(f"O dado do Jogador 2 caiu em {dado2}")

if (dado1 > dado2):
    print(f"Jogador 1 avance {dado1} casas")
elif (dado1 < dado2):
    print(f"Jogador 2 avance {dado2} casas")
else:
    print("Empate")


