def checar(nome, volta, total):
    if volta==total:
        print(f"parabens todos os {total} {nome} voltaram!")
    elif volta<total:
        print(f"faltam {total-volta} {nome} voLtarem")
    else:
        print(f"voltaram {volta-total} {nome} a mais")

print("------bem vindo------")
print("-qual grupo animal deseja fazer o calculo? \n-porcos\n-vacas\n-golfinhos")
escolha=input("R: ").lower()

if escolha in ["porcos","vacas","golfinhos",]:
    total_animais=int(input(f"quantos {escolha} voçê tem no total? R: "))
    volta_animais=int(input(f"quantos {escolha} voltaram no total? R: "))
    checar(escolha, volta_animais, total_animais)