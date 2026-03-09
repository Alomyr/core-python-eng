palavra = "test"
tentativas = ""
print("adivinhe a plavra")
while not (tentativas == palavra):
    jogada = str(input("Digite sua jogada: "))
    if jogada.isalpha():
        if jogada in palavra:
            tentativas += jogada
            if jogada == palavra:
                print("vc ganhou")
                break
            print("existe essa letra")

        for index in range(len(palavra)):
            if palavra[index] in tentativas:
                print(palavra[index], end="")
            else:
                print("_", end="")
        print()
    else:
        print("deve ser apenas letras")
