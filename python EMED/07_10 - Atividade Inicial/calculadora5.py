numero1 = int(input("insira o primeiro numero: "))
numero2 = int(input("insira o segundo numero: "))
escolha = int(input("voce deseja 1-somar, 2-subtrair, 3-multiplicar, 4-dividir: "))

if escolha == 1:
    print(numero1 + numero2)
elif escolha == 2:
    print(numero1 - numero2)
elif escolha == 3:
    print(numero1 * numero2)
elif escolha == 4:
    print(numero1 / numero2)