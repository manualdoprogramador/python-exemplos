import  random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Forca!")
    print("*********************************")

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            marcar_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print(f"Você errou {erros} de {7} tentativas")

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns você acertou!!!")
    else:
        print("Você perdeu!!!")

def carrega_palavra_secreta():
    arquivo = open("/Users/gutofilipe93/Documents/CANAL YOUTUBE/python-exemplos/Jogos/adivinhacao/palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def marcar_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index += 1

jogar()        