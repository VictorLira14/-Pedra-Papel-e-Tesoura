import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    jogador = input("Escolha (pedra, papel, tesoura): ").lower()

    if jogador not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return jogar()

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

if __name__ == "__main__":
    jogar()