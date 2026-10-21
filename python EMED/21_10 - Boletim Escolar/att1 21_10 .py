import tkinter as tk
from tkinter import messagebox


def calcular():
    nome = campo_nome.get().strip()
    turma = campo_turma.get().strip()

    if nome == "" or turma == "":
        messagebox.showwarning("Atenção", "Preencha nome e turma!")
        return

    try:
        nota1 = float(campo_nota1.get())
        nota2 = float(campo_nota2.get())
        nota3 = float(campo_nota3.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite notas numéricas!")
        return

    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        messagebox.showwarning(
            "Notas inválidas",
            "As notas devem estar entre 0 e 10."
        )
        return

    media = (nota1 + nota2 + nota3) / 3

    if media >= 9:
        situacao = "Excelente aprovado!"
    elif media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    resultado.config(
        text=f"{nome} ({turma}) | Média: {media:.1f} | {situacao}"
    )


def limpar():
    campo_nome.delete(0, tk.END)
    campo_turma.delete(0, tk.END)
    campo_nota1.delete(0, tk.END)
    campo_nota2.delete(0, tk.END)
    campo_nota3.delete(0, tk.END)

    resultado.config(text="Resultado aparecerá aqui.")


janela = tk.Tk()
janela.title("Boletim Escolar - ENZO NUÑEZ")
janela.geometry("540x490")

tk.Label(
    janela,
    text="BOLETIM ESCOLAR - ENZO NUÑEZ",
    font=("Arial", 18, "bold")
).pack(pady=16)

tk.Label(janela, text="Nome:").pack()
campo_nome = tk.Entry(janela, width=38)
campo_nome.pack(pady=4)

tk.Label(janela, text="Turma:").pack()
campo_turma = tk.Entry(janela, width=38)
campo_turma.pack(pady=4)

tk.Label(janela, text="Nota 1:").pack()
campo_nota1 = tk.Entry(janela, width=20)
campo_nota1.pack(pady=4)

tk.Label(janela, text="Nota 2:").pack()
campo_nota2 = tk.Entry(janela, width=20)
campo_nota2.pack(pady=4)

tk.Label(janela, text="Nota 3:").pack()
campo_nota3 = tk.Entry(janela, width=20)
campo_nota3.pack(pady=4)

tk.Button(
    janela,
    text="Calcular média",
    command=calcular
).pack(pady=8)

tk.Button(
    janela,
    text="Limpar",
    command=limpar
).pack(pady=4)

resultado = tk.Label(
    janela,
    text="Resultado aparecerá aqui.",
    wraplength=480
)
resultado.pack(pady=12)

janela.mainloop()

