import tkinter as tk

def somar():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())

    soma=numero1+numero2

    resultado.config(text="Resultado:"+ str(soma))



janela=tk.Tk()
janela.title("Somar dois números")
janela.geometry("350x300")




texto1=tk.Label(janela, text="Digite o primeiro número: ")
texto1.pack(pady=5)
entrada1=tk.Entry(janela)
entrada1.pack()


texto2=tk.Label(janela, text="Digite o segundo número: ")
texto2.pack(pady=5)
entrada2=tk.Entry(janela)
entrada2.pack()


botao=tk.Button(janela, text="Somar", command=somar)
botao.pack(pady=20)

resultado=tk.Label(janela,text="Resultado: ")
resultado.pack()

janela.mainloop()