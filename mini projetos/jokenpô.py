from random import choice
print('BEM VINDO AO JOGO DE JOKENPÔ')
while True:
    q_jogo=int(input('Você deseja jogar com um jogador ou dois? [1] ou [2]: '))

    if q_jogo==1:
        jogador=input(f'ESCOLHA UM: PEDRA , PAPEL OU TESOURA: ').lower()
        escolhas=['pedra', 'papel', 'tesoura']
        computador= choice(escolhas)

        if jogador == computador:
            print('Empate ou seja, sem ganhadores')
        elif ((jogador=='pedra' and computador=='tesoura') or (jogador=='tesoura'and computador=='papel') or (jogador=='papel'and computador=='pedra')):
            print(f'Parabens, VOCÊ GANHOU: (você){jogador}X{computador}(rôbo)')
        elif ((jogador=='pedra'and computador=='papel')or(jogador=='tesoura' and computador=='pedra')or(jogador=='papel' and computador=='tesoura')):
            print(f'Que pena, VOCÊ PERDEU: (você){jogador}X{computador}(rôbo)')
    elif q_jogo==2:
        escolhas=['pedra', 'papel', 'tesoura']
        jogador1=input(f'(JOGADOR 1) ESCOLHA UM: PEDRA , PAPEL OU TESOURA: ').lower()
        jogador2=input(f'(JOGADOR 2) ESCOLHA UM: PEDRA , PAPEL OU TESOURA: ').lower()
        

        if jogador1 == jogador2:
            print('Empate ou seja, sem ganhadores')
        elif ((jogador1=='pedra' and jogador2=='tesoura') or (jogador1=='tesoura'and jogador2=='papel') or (jogador1=='papel'and jogador2=='pedra')):
            print(f'Parabéns, JOGADOR 1 GANHOU!: (JOGADOR 1) {jogador1} X {jogador2} (JOGADOR 2)')
        elif ((jogador1=='pedra'and jogador2=='papel')or(jogador1=='tesoura' and jogador2=='pedra')or(jogador1=='papel' and jogador2=='tesoura')):
            print(f'Parabens, JOGADOR 2 VOCÊ GANHOU!: (JOGADOR 1){jogador1}X{jogador2}(JOGADOR 2)')
    repetir=input('Deseja jogar denovo? [s] [n]:')
    if repetir != 's':
        break
print('obrigado por jogar!')