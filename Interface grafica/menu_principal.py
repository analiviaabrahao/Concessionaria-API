import tkinter as tk
import customtkinter as ctk
import subprocess
from PIL import Image, ImageTk

# Funções para abrir as janelas específicas
def abrir_veiculo():
    subprocess.Popen([
        '/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/myenv/bin/python',
        "/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/Interface grafica/gui_Veiculo.py"
    ])

def abrir_cliente():
    subprocess.Popen([
        '/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/myenv/bin/python',
        "/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/Interface grafica/gui_Cliente.py"
    ])

def abrir_negociacao():
    subprocess.Popen([n
        '/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/myenv/bin/python',
        "/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/Interface grafica/gui_Negociacao.py"
    ])

# Criação da janela principal
root = ctk.CTk()
root.title("Concessionária - Menu Principal")
root.geometry("800x600")  # Ajuste a geometria para o tamanho da imagem

imagem_fundo = Image.open("ana_motors.png")
imagem_fundo = imagem_fundo.resize((800, 600), Image.LANCZOS)
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, anchor="nw", image=imagem_fundo_tk)

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# Botões
btn_veiculo = ctk.CTkButton(root, text="Gerenciar Veículos", command=abrir_veiculo, width=200, height=50)
btn_veiculo.place(relx=0.95, rely=0.4, anchor="e")  # Usando place para posicionar o botão

btn_cliente = ctk.CTkButton(root, text="Gerenciar Clientes", command=abrir_cliente, width=200, height=50)
btn_cliente.place(relx=0.95, rely=0.5, anchor="e")  # Usando place para posicionar o botão

btn_negociacao = ctk.CTkButton(root, text="Gerenciar Negociações", command=abrir_negociacao, width=200, height=50)
btn_negociacao.place(relx=0.95, rely=0.6, anchor="e")  # Usando place para posicionar o botão

# Rodapé
rodape = ctk.CTkLabel(root, text="© 2024 Concessionária Ana motors", font=("Arial", 10))
rodape.place(relx=0.5, rely=0.95, anchor="center")  # Posicionando o rodapé na parte inferior

# Iniciar a interface
root.mainloop()



















