import random

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)  # 1 até 100
total_de_tentativas = 0

print("Qual o nivel de dificuldade?")
print("1 - Fácil, 2 - Medio, 3 - Difícil")
nivel = int(input("Digite o nivel: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativas {} de {}".format(rodada, total_de_tentativas))
    valor_escolhido_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", valor_escolhido_str)
    valor_escolhido = int(valor_escolhido_str)

    if (valor_escolhido < 1 or valor_escolhido > 100):
        print("Numero invalido. O número deve estar entre 1 e 100")
        continue

    acertou = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto

    if (acertou):
        print(f"Parabéns você acertou em {total_de_tentativas} tentativas!")
        break
    else:
        if (maior):
            print("Você errou, o chute foi maior que o numero secreto")
        elif (menor):
            print("Você errou, o chute foi menor que o valor secreto")
        

print("Fim do jogo")