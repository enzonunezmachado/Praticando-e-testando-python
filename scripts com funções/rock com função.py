import random

def pc_choise():
    random_computer=random.randint(0,2)
    if random_computer==0:
        choice_computer='pedra'
    elif random_computer==1:
        choice_computer='papel'   
    else:
        choice_computer='tesoura'
    return choice_computer
while True:
    print('BEM VINDO AO JOGO DE JOKENPÔ')

    move_pc=pc_choise()

    player=input('escolha pedra, papel ou tesoura : ')

    if move_pc==player:
        escolha=input('empate jogar novamente? [s/n]: ')
    elif (move_pc == 'papel' and player == 'pedra') or \
         (move_pc == 'pedra' and player == 'tesoura') or \
         (move_pc == 'tesoura' and player == 'papel'):
        escolha = input('Você ganhou! Deseja jogar novamente? [s/n]: ')
    else:
        escolha=input(f'você ganhou! deseja jogar novamente? [s/n]: ')
    if escolha!='s':
        break
print('obrigado por jogar!')
