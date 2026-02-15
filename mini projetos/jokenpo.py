import random
while True:
    escolhas=['pedra', 'papel', 'tesoura']
    escolhas_pc=random.choice(escolhas)
    player=input('escolha pedra papel ou tesoura: ').lower()
    if escolhas_pc==player:
        print('empate')
    elif (escolhas_pc=='pedra' and player=='tesoura')or(escolhas_pc=='tesoura' and player=='papel')or(escolhas_pc=='papel'and player=='pedra'):
        print('perdeu')
    else:
        print('ganhou')
    jogar=input('deseja jogar novamente? [s/n]')
    if jogar!='s':
        break
print('obrigado por jogar!')
