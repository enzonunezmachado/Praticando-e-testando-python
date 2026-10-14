import tkinter as tk

def media():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())

    media_d_2=(numero1+numero2)/2

    resultado.config(text="Resultado:"+ str(media_d_2))



janela=tk.Tk()
janela.title("Média de dois numeros")
janela.geometry("500x350")




texto1=tk.Label(janela, text="Digite o primeiro número: ")
texto1.pack(pady=5)
entrada1=tk.Entry(janela)
entrada1.pack()


texto2=tk.Label(janela, text="Digite o segundo número: ")
texto2.pack(pady=5)
entrada2=tk.Entry(janela)
entrada2.pack()


botao=tk.Button(janela, text="Calcular média", command=media)
botao.pack(pady=20)

resultado=tk.Label(janela,text="Resultado: ")
resultado.pack()

janela.mainloop()