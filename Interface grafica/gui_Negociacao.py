import datetime
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
import requests

def list_negociacoes():
    # Atualiza a lista de negociações na interface
    for row in tree.get_children():
        tree.delete(row)

    response = requests.get("http://localhost:8080/api/negociacoes")
    negociacoes = response.json()
    for neg in negociacoes:
        tree.insert("", "end", values=(
            neg['id'],
            neg['valor_fipe'],
            neg['valor_venda'],
            neg['valor_compra'],
            neg['status'],
            neg['id_veiculo'],
            neg['id_cliente'],
            neg['data_contrato']
        ))

def save_negociacao():
    id = int(entry_id.get())
    valor_fipe = int(entry_valor_fipe.get())
    valor_venda = int(entry_valor_venda.get())
    valor_compra = int(entry_valor_compra.get())
    status = entry_status.get()
    id_veiculo = int(entry_id_veiculo.get())
    id_cliente = int(entry_id_cliente.get())
    data_contrato = datetime.datetime.strptime(entry_data_contrato.get(), "%Y-%m-%d"). date() 

    # Dados da negociação
    data = {
        "id": id,
        "valor_fipe": valor_fipe,
        "valor_venda": valor_venda,
        "valor_compra": valor_compra,
        "status": status,
        "id_veiculo": id_veiculo,
        "id_cliente": id_cliente,
        "data_contrato": str(data_contrato)
    }

    response = requests.post("http://localhost:8080/api/negociacoes", data=data)
    neg = response.json()
    tree.insert("", "end", values=(neg['id'], neg['valor_fipe'], neg['valor_venda'], neg['valor_compra'], neg['status'], neg['id_veiculo'], neg['id_cliente'], neg['data_contrato']))
    messagebox.showinfo("Sucesso", "Negociação salva com sucesso!")
    #else:
     #   messagebox.showerror("Erro", f"Falha ao salvar negociação: {response.text}")

def delete_negociacao():
    id = int(entry_id.get())
    response = requests.delete(f"http://localhost:8080/api/negociacoes/{id}")
   # if response.status_code == 200:
    list_negociacoes()
    messagebox.showinfo("Sucesso", "Negociação excluída com sucesso!")
    #else:
     #   messagebox.showerror("Erro", f"Falha ao excluir negociação: {response.text}")



# Criação da janela principal
root = ctk.CTk()
root.title("Cadastro de Negociações")
root.geometry("2000x500")

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Labels e entradas para os dados da negociação
ctk.CTkLabel(root, text="ID:").grid(row=0, column=0, padx=8, pady=5, sticky="w")
entry_id = ctk.CTkEntry(root, placeholder_text="Digite o ID")
entry_id.grid(row=0, column=1, padx=8, pady=5)

ctk.CTkLabel(root, text="Valor FIPE:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
entry_valor_fipe = ctk.CTkEntry(root, placeholder_text="Digite o valor FIPE")
entry_valor_fipe.grid(row=0, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Valor Venda:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_valor_venda = ctk.CTkEntry(root, placeholder_text="Digite o valor da venda")
entry_valor_venda.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="Valor Compra:").grid(row=1, column=2, padx=10, pady=5, sticky="w")
entry_valor_compra = ctk.CTkEntry(root, placeholder_text="Digite o valor compra")
entry_valor_compra.grid(row=1, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Status:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_status = ctk.CTkEntry(root, placeholder_text="Digite o status")
entry_status.grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="ID Veículo:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
entry_id_veiculo = ctk.CTkEntry(root, placeholder_text="Digite o ID do veículo")
entry_id_veiculo.grid(row=2, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="ID Cliente:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_id_cliente = ctk.CTkEntry(root, placeholder_text="Digite o ID do cliente")
entry_id_cliente.grid(row=3, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="Data Contrato:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
entry_data_contrato = ctk.CTkEntry(root, placeholder_text="Digite a data contrato")
entry_data_contrato.grid(row=3, column=3, padx=10, pady=5)

# Botões de ação
save_button = ctk.CTkButton(root, text="Salvar Negociação", command=save_negociacao)
save_button.grid(row=4, column=0, pady=10, padx=10, sticky="e")

# delete_button = ctk.CTkButton(root, text="Excluir Negociação", command= delete_negociacao) 
# delete_button.grid(row=4, column=1, pady=10, padx=10, sticky="e")




# Estilo para a árvore (Treeview)
style = ttk.Style()
style.configure("Custom.Treeview",
                background="lightgray",
                foreground="black",
                fieldbackground="white",
                rowheight=25)
style.configure("Custom.Treeview.Heading",
                background="gray",
                foreground="white",
                font=('Arial', 10, 'bold'))

# Árvore para exibição das negociações
tree = ttk.Treeview(root, columns=("ID", "Valor FIPE", "Valor da Venda", "Valor da Compra", "Status", "ID do Veículo", "ID do Cliente", "Data do Contrato"), show="headings", style="Custom.Treeview")
tree.heading("ID", text="ID")
tree.heading("Valor FIPE", text="Valor FIPE")
tree.heading("Valor da Venda", text="Valor da Venda")
tree.heading("Valor da Compra", text="Valor da Compra")
tree.heading("Status", text="Status")
tree.heading("ID do Veículo", text="ID do Veículo")
tree.heading("ID do Cliente", text="ID do Cliente")
tree.heading("Data do Contrato", text="Data do Contrato")
tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Configurar o layout responsivo
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1, uniform= "equal")
root.grid_columnconfigure(1, weight=1,uniform= "equal")
list_negociacoes()

# Iniciar o CustomTkinter
root.mainloop()