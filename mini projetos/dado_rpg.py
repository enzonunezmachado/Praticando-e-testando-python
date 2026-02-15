import random
while True:
    faces_dado = [
        """
    +-----------+
    |           |
    |     ●     |
    |           |
    +-----------+
    """,
        """
    +-----------+
    | ●         |
    |           |
    |         ● |
    +-----------+
    """,
        """
    +-----------+
    | ●         |
    |     ●     |
    |         ● |
    +-----------+
    """,
        """
    +-----------+
    | ●       ● |
    |           |
    | ●       ● |
    +-----------+
    """,
        """
    +-----------+
    | ●       ● |
    |     ●     |
    | ●       ● |
    +-----------+
    """,
        """
    +-----------+
    | ●   ●   ● |
    |           |
    | ●   ●   ● |
    +-----------+
    """
    ]
    escolha_pc=random.choice(faces_dado)
    print(escolha_pc)
    escolha=input('deseja jogar novamente o dado? [s/n]: ')
    if escolha!='s':
        break
print('programa finalizado!')
