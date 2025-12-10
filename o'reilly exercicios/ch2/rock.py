import random
random_computer=random.randint(0,2)

if random_computer==0:
    choice_computer='rock'
elif random_computer==1:
    choice_computer='paper'
else:
    choice_computer='scissors'

user_choice=input('chose: paper, rock or scissors: ')
print('you choice', user_choice,'the computer choises', choice_computer)