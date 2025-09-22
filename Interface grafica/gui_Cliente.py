import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
import requests

def list_clientes():
    # Atualiza a lista de clientes na interface
    for row in tree.get_children():
        tree.delete(row)

    response = requests.get("http://localhost:8080/api/clientes")
    clientes = response.json()
    for cliente in clientes:
        tree.insert("", "end", values=(
            cliente['id'],
            cliente['nome'],
            cliente['cpf'],
            cliente['cnh'],
            cliente['email'],
            cliente['telefone']
        ))

def save_cliente():
    id = int(entry_id.get())
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    cnh = entry_cnh.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    # Dados do cliente
    data = {
        "id": id,
        "nome": nome,
        "cpf": cpf,
        "cnh": cnh,
        "email": email,
        "telefone": telefone
    }

    response = requests.post("http://localhost:8080/api/clientes", data=data)
    cliente = response.json()
    tree.insert("", "end", values=(cliente['id'], cliente['nome'], cliente['cpf'], cliente['cnh'], cliente['email'], cliente['telefone']))
    messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")






def delete_cliente():
    id = int(entry_id.get())
    response = requests.delete(f"http://localhost:8080/api/clientes/{id}")
    #if response.status_code == 200:  # Sucesso ao excluir
    list_clientes()
    messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
   # else:
    #    messagebox.showerror("Erro", "Falha ao excluir o cliente!")


def abrir_conta():
    subprocess.Popen([
       '/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/myenv/bin/python',
       "/home/Downloads/Concessionaria/CONCESSIONARIA-/Concessionaria/Interface grafica/gui_Conta.py"
    ])

# Criação da janela principal
root = ctk.CTk()
root.title("Cadastro de Clientes")
root.geometry("1000x450")

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Tema: "blue", "dark-blue", "green"

# Labels e entradas para os dados do cliente
ctk.CTkLabel(root, text="ID:").grid(row=0, column=0, padx=8, pady=5, sticky="w")
entry_id = ctk.CTkEntry(root, placeholder_text="Digite o ID")
entry_id.grid(row=0, column=1, padx=8, pady=5)

ctk.CTkLabel(root, text="Nome:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
entry_nome = ctk.CTkEntry(root, placeholder_text="Digite o Nome")
entry_nome.grid(row=0, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="CPF:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_cpf = ctk.CTkEntry(root, placeholder_text="Digite o CPF")
entry_cpf.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="CNH:").grid(row=1, column=2, padx=10, pady=5, sticky="w")
entry_cnh = ctk.CTkEntry(root, placeholder_text="Digite a CNH")
entry_cnh.grid(row=1, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_email = ctk.CTkEntry(root, placeholder_text="Digite o Email")
entry_email.grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="Telefone:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
entry_telefone = ctk.CTkEntry(root, placeholder_text="Digite o Telefone")
entry_telefone.grid(row=2, column=3, padx=10, pady=5)

#Botões de ação
save_button = ctk.CTkButton(root, text="Salvar Cliente", command=save_cliente)
save_button.grid(row=3, column=0, pady=10, padx=10)

btn_conta = ctk.CTkButton(root, text="Gerenciar Contas Bancarias", command=abrir_conta)
btn_conta.grid( row=3, column=1, pady=10, padx=10)

delete_button = ctk.CTkButton(root, text="Excluir Cliente", command=delete_cliente)
delete_button.grid(row=3, column=2, pady=10, padx=10)








# Estilo para a árvore (Treeview)
style = ttk.Style()
style.configure("Custom.Treeview",
                background="lightgray",  # Cor de fundo
                foreground="black",  # Cor do texto
                fieldbackground="white",  # Cor de fundo das células
                rowheight=25)  # Altura das linhas
style.configure("Custom.Treeview.Heading",
                background="gray",  # Cor de fundo do cabeçalho
                foreground="white",  # Cor do texto do cabeçalho
                font=('Arial', 10, 'bold'))  # Fonte do cabeçalho

# Árvore para exibição dos clientes (Treeview do ttk) com estilo customizado
tree = ttk.Treeview(root, columns=("ID", "Nome", "CPF", "CNH", "Email", "Telefone"), show="headings", style="Custom.Treeview")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("CPF", text="CPF")
tree.heading("CNH", text="CNH")
tree.heading("Email", text="Email")
tree.heading("Telefone", text="Telefone")
tree.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Configurar o layout responsivo
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

list_clientes()

# Iniciar o CustomTkinter
root.mainloop()
