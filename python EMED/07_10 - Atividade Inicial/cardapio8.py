print("=" * 30)
print("          CARDÁPIO")
print("=" * 30)

print("1 - Hambúrguer      R$ 18,00")
print("2 - Batata frita    R$ 12,00")
print("3 - Refrigerante    R$ 7,00")

print("=" * 30)

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print("\nVocê escolheu: Hambúrguer")
    print("Preço: R$ 18,00")

elif opcao == 2:
    print("\nVocê escolheu: Batata frita")
    print("Preço: R$ 12,00")

else:
    print("\nVocê escolheu: Refrigerante")
    print("Preço: R$ 7,00")

