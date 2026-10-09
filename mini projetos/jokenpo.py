import random
while True:
    escolhas=['pedra', 'papel', 'tesoura']
    escolhas_pc=random.choice(escolhas)
    player=input('Escolha pedra papel ou tesoura: ').lower()
    if escolhas_pc==player:
        print('Empate')
    elif (escolhas_pc=='pedra' and player=='tesoura')or\
    (escolhas_pc=='tesoura' and player=='papel')or \
    (escolhas_pc=='papel'and player=='pedra'):
        print('Perdeu')
    else:
        print('Ganhou')
    jogar=input('Deseja jogar novamente? [s/n]')
    if jogar!='s':
        break
print('Obrigado por jogar!')
