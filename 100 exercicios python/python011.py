import math
altura_m=float(input('qual a altura em metros da parede?: '))
largura_m=float(input('qual a largura em metros da parede?: '))
area_parede=altura_m*largura_m
l_tinta=math.ceil(area_parede/2)
print(f'A parede tem a dimensão de {largura_m}X{altura_m} sua área é :{area_parede:.2f}m²')
print(f'E será necessario {l_tinta:.0f} litros de tinta para pintar totalmente a parede. ')