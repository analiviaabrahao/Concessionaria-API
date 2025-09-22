import tkinter as tk
from tkinter import messagebox, ttk
import tkinter
import customtkinter as ctk
import requests

# Função para listar as contas bancárias
def list_contas_bancarias():
    # Atualiza a lista de contas bancárias na interface
    for row in tree.get_children():
        tree.delete(row)

    response = requests.get("http://localhost:8080/api/contas")
    contas = response.json()
    for conta in contas:
        tree.insert("", "end", values=(
            conta['id'],
            conta['agencia'],
            conta['banco'],
            conta['status'], 
            conta['id_cliente']
        ))

# Função para salvar uma nova conta bancária
def save_conta_bancaria():
    id = int(entry_id.get())
    agencia = entry_agencia.get()
    banco = entry_banco.get()
    status = entry_status.get()
    id_cliente = int(entry_id_cliente.get())
    

    # Dados da conta bancária
    data = {
        "id": id,
        "agencia": agencia,
        "banco": banco,
        "status": status,
        "id_cliente": id_cliente
    }

    response = requests.post("http://localhost:8080/api/contas", data=data)
    #if response.status_code == 201:  # 201 é o código de sucesso para criação
    conta = response.json()
    tree.insert("", "end", values=(conta['id'], conta['agencia'], conta['banco'], conta['status'], conta['id_cliente']))
    messagebox.showinfo("Sucesso", "Conta bancária inserida com sucesso!")
    #else:
     #   messagebox.showerror("Erro", f"Falha ao inserir conta bancária: {response.text}")

# Função para excluir uma conta bancária
# def delete_conta_bancaria():
#     id = int(entry_id.get())
#     response = requests.delete(f"http://localhost:8080/api/contas/{id}")
#    # if response.status_code == 200:
#     list_contas_bancarias()
#     messagebox.showinfo("Sucesso", "Conta bancária excluída com sucesso!")
#     #else:
#      #   messagebox.showerror("Erro", "Falha ao excluir a conta bancária!")

# Criação da janela principal
root = ctk.CTk()
root.title("Cadastro de Contas Bancárias")
root.geometry("1000x500")

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Tema: "blue", "dark-blue", "green"

# Labels e entradas para os dados da conta bancária
ctk.CTkLabel(root, text="ID:").grid(row=0, column=0, padx=8, pady=5, sticky="w")
entry_id = ctk.CTkEntry(root, placeholder_text="digite o Id")
entry_id.grid(row=0, column=1, padx=8, pady=5)

ctk.CTkLabel(root, text="Agência:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
entry_agencia = ctk.CTkEntry(root, placeholder_text="digite a Agência")
entry_agencia.grid(row=0, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Banco:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_banco = ctk.CTkEntry(root, placeholder_text="digite o Banco")
entry_banco.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="Status:").grid(row=1, column=2, padx=10, pady=5, sticky="w")
entry_status = ctk.CTkEntry(root, placeholder_text="digite o Status")
entry_status.grid(row=1, column=3, padx=10, pady=5)

# Agora o campo "Id do Cliente" vai para a linha 2
ctk.CTkLabel(root, text="Id do Cliente:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_id_cliente = ctk.CTkEntry(root, placeholder_text="digite o Id do Cliente")
entry_id_cliente.grid(row=2, column=1, padx=10, pady=5)


# Botões de ação
save_button = ctk.CTkButton(root, text="Salvar Conta Bancária", command=save_conta_bancaria)
save_button.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

# delete_button = ctk.CTkButton(root, text="Excluir Conta Bancária", command=delete_conta_bancaria)
# delete_button.grid(row=4, column=2, pady=10, padx=10, sticky="ew")

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

# Árvore para exibição das contas bancárias (Treeview do ttk) com estilo customizado
tree = ttk.Treeview(root, columns=("ID", "Agência", "Banco", "Status", "Id do Cliente"), show="headings", style="Custom.Treeview")
tree.heading("ID", text="ID")
tree.heading("Agência", text="Agência")
tree.heading("Banco", text="Banco")
tree.heading("Status", text="Status")
tree.heading("Id do Cliente", text="Id do Cliente")
tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Configurar o layout responsivo
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

list_contas_bancarias()  # Carrega as contas bancárias ao iniciar

# Iniciar o CustomTkinter
root.mainloop()