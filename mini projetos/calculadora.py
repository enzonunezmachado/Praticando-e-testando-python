inicio = True

continuar = True

math=__import__('math')

fractions=__import__('fractions')

while inicio:

    while continuar:

        print("\n Escolha qual operação deseja efetuar: ")

        operação=input(" adição[a]          exponenciação[e]\n subtração[s]       raiz[r]\n multiplicação[m]   porcentagem[p]\n divisão[d]         fatorial[f]\n logaritimo[l]      juros[j]\n somatorio[sm]\n\n escolha: ").lower() .strip()

        if operação =="r":

            numero3=int(input(" Escolha qual número deseja calcular a raiz: "))             #raiz

            numero8=int(input(" Escolha qual indice deseja calcular: "))

            if numero3 < 0 and numero8 % 2 == 0:

                print(" Não existe em ℝ")

            else:

                if numero3 < 0:

                    print(" √ de",numero3, "= \033[33m",-((-numero3)**(1/numero8)),"\033[0m")

                else:

                    print(" √ de",numero3, "= \033[33m", (numero3**(1/numero8)),"\033[0m")

        elif operação=="sm":

            lim_inf = int(input(" Digite o limite inferior: "))

            lim_sup = int(input(" Digite o limite superior: "))

            funç = input(" Digite a expressão em função de i (ex.: i**2, 2*i+1): ")

            resultado = sum(eval(funç) for i in range(lim_inf, lim_sup + 1))

            print(f" O somatorio ∑ de {lim_sup} é = {resultado}")

        elif operação=="j":

            tipojuros=input(" Juros simples ou compostos?(js/jc) ")

            if tipojuros=="js":

                c=float(input(" Capital inicial: "))

                i=float(input(" Taxa de juros mensal: "))/100 

                t=int(input(" Tempo em meses: "))

                jsv=c*i*t

                print(f"\n Juros simples: R${jsv}")

            elif tipojuros=="jc":

                c=float(input(" Capital inicial: "))

                i=float(input(" Taxa de juros mensal: "))/100

                t=int(input(" Tempo em meses: "))

                jcv=c*(1+i)**t

                print(f"\n Juros simples: R${jcv}")

            elif tipojuros not in ["js","jc"]:

                print(" Não há uma operação para o juros que você escolheu.")

                resposta1 = input(" Deseja reiniciar? (y/n): ")

                if resposta1.lower() == 'y':

                    continuar = True

                elif resposta1.lower() == 'n':

                    print(" Programa encerrado.")

                    break

        elif operação=="p":

            numero4=int(input(" Escolha qual número deseja calcular a porcentagem? "))       #porcentagem

            numero5=int(input(" Escolha qual o valor da porcentagem que deseja calcular: "))

            print(numero5, "% de", numero4,"é\033[033m", numero4/100*(numero5),"\033[0m")

        elif operação== "f":

            numero6=int(input(" Escolha um numero para calcular seu fatorial. "))             #fatorial

            resultadof=math.factorial(numero6) 

            print(" O fatorial do numero", numero6, "é =\033[033m", resultadof,"\033[0m")

        elif operação not in ["a", "s", "m", "d", "e", "r", "p", "f","l","sm"]:

            print(" Não há uma operação para a letra que você escolheu.")

            resposta2 = input(" Deseja reiniciar? (y/n): ")

            if resposta2.lower() == 'y':

                continuar = True

                continue

            elif resposta2.lower() == 'n':

                print(" Programa encerrado.")

                break

        elif operação=="l":

            numero7=int(input(" Escolha um número para calcular seu logaritimo: "))

            base=int(input(" Escolha um número para a base do logaritimando: "))

            resultadol=math.log(numero7, base)                                                #logaritimo

            print(" O logaritimo do número", numero7, "na base",base,"é\033[033m",resultadol,"\033[0m")

        else:

            numero1=int(input(" Escolha seu primeiro número: "))

            numero2=int(input(" Escolha seu segundo número: "))

            if operação=="a":

                print( numero1,"+", numero2,"= \033[033m",numero1+numero2,"\033[0m")          #soma

            elif operação=="s":

                print( numero1,"-", numero2,"= \033[033m",numero1-numero2,"\033[0m")          #subtração

            elif operação=="m":

                print( numero1,"x", numero2,"= \033[033m",numero1*numero2,"\033[0m")          #multiplicação

            elif operação=="d":

                if numero2 == 0: 

                    print(" Não é possivel dividir esse número por zero.")

                    resposta1=input("Deseja reiniciar? (y/n): ")

                    if resposta1.lower() == "y":

                        continuar = True 

                        continue

                    elif resposta1.lower() == "n":

                        print(" Programa encerrado.")

                        break

                print( numero1,"/", numero2,"= \033[033m",numero1/numero2,"\033[0m")          #divisão

            elif operação=="e":

                x=fractions.Fraction(numero1)**numero2

                y=fractions.Fraction(x)

                if numero2<0:

                    print( numero1,"^",numero2,"= \033[033m",y,"\033[0m ou \033[033m",numero1**numero2,"\033[0m")   #exponenciação

                else:

                    print( numero1,"^",numero2,"= \033[033m",y,"\033[0m")

        continuar = False

        resposta3=input(" Deseja fazer outra operação? (y/n): ")

        if resposta3.lower() == "y":

            continuar = True 

            continue

        elif resposta3.lower() == "n":

            print(" Programa encerrado.")

    break
 