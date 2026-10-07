import random
while True:
    jogador=input('escolha entre copo_1, copo_2 ou copo_3? [1], [2], [3]: ')
    escolha=('1','2','3')
    posição_bola=random.choice(escolha)
    if posição_bola == jogador:
        print('acertou!')
    else:
        print('errou!')
    continuar=input('deseja jogar denovo? [s/n]: ')
    if continuar!='s':
        break
print('obrigado por jogar!')
