import tkinter as tk
from tkinter import messagebox,  ttk
import tkinter
import customtkinter as ctk
import requests

# janela = tkinter.Tk()

# janela.mainloop()


def list_veiculos():
    # Atualiza a lista de veículos na interface (o código para buscar e atualizar a árvore)
    for row in tree.get_children():
        tree.delete(row)

    response = requests.get("http://localhost:8080/api/veiculos")
    veiculos = response.json()
    for veic in veiculos:
        tree.insert("", "end", values=(
            veic['id'],
            veic['tipo'],
            veic['placa'],
            veic['marca'],
            veic['modelo'],
            veic['pendencia'],
            veic['renavam'],
            veic['km']
        ))

def save_veiculo():
    id = int(entry_id.get())
    tipo = entry_tipo.get()
    placa = entry_placa.get()
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    pendencia = entry_pendencia.get()
    renavam = int(entry_renavam.get())
    km = float(entry_km.get())


    # Dados do veículo
    data = {
        "id": id,
        "tipo": tipo,
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "pendencia": pendencia,
        "renavam": renavam,
        "km": km
    }


    response = requests.post("http://localhost:8080/api/veiculos", data=data)
    veic = response.json()
    tree.insert("", "end", values=(veic['id'], veic['tipo'], veic['placa'], veic['marca'], veic['modelo'], veic['pendencia'], veic['renavam'], veic['km']))
    messagebox.showinfo("Ok!", "Veiculo inserido com sucesso!")





def delete_veiculo():
    id = int(entry_id.get())
    response = requests.delete(f"http://localhost:8080/api/veiculos/{id}")
  #  if response.status_code == 200:
    list_veiculos()
    messagebox.showinfo("Sucesso", "Veículo excluído com sucesso!")
   # else:
    #    messagebox.showerror("Erro", "Falha ao excluir o veículo!")



# Criação da janela principal
root = ctk.CTk()
root.title("Cadastro de Veículos")
root.geometry("2000x500")




# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Tema: "blue", "dark-blue", "green"




# Labels e entradas para os dados do veículo
ctk.CTkLabel(root, text="ID:").grid(row=0, column=0, padx=8, pady=5, sticky="w")
entry_id = ctk.CTkEntry(root, placeholder_text= "digite o Id")
entry_id.grid(row=0, column=1, padx=8, pady=5)

ctk.CTkLabel(root, text="Tipo:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
entry_tipo = ctk.CTkEntry(root, placeholder_text= "digite o Tipo")
entry_tipo.grid(row=0, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Placa:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_placa = ctk.CTkEntry(root, placeholder_text= "digite a Placa")
entry_placa.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="Marca:").grid(row=1, column=2, padx=10, pady=5, sticky="w")
entry_marca = ctk.CTkEntry(root, placeholder_text= "digite a Marca")
entry_marca.grid(row=1, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_modelo = ctk.CTkEntry(root, placeholder_text= "digite o Modelo")
entry_modelo.grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="Pendência:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
entry_pendencia = ctk.CTkEntry(root, placeholder_text= "digite a Pendência")
entry_pendencia.grid(row=2, column=3, padx=10, pady=5)

ctk.CTkLabel(root, text="Renavam:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_renavam = ctk.CTkEntry(root, placeholder_text= "digite o renavam")
entry_renavam.grid(row=3, column=1, padx=10, pady=5)

ctk.CTkLabel(root, text="KM:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
entry_km = ctk.CTkEntry(root, placeholder_text= "digite o KM")
entry_km.grid(row=3, column=3, padx=10, pady=5)

# Botões de ação
save_button = ctk.CTkButton(root, text="Salvar Veículo", command=save_veiculo)
save_button.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

delete_button = ctk.CTkButton(root, text="Excluir Veículo", command= delete_veiculo) 
delete_button.grid(row=4, column=2, pady=10, padx=10, sticky="ew")

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

# Árvore para exibição dos veículos (Treeview do ttk) com estilo customizado
tree = ttk.Treeview(root, columns=("ID", "Tipo", "Placa", "Marca", "Modelo", "Pendência", "Renavam", "KM"), show="headings", style="Custom.Treeview")
tree.heading("ID", text="ID")
tree.heading("Tipo", text="Tipo")
tree.heading("Placa", text="Placa")
tree.heading("Marca", text="Marca")
tree.heading("Modelo", text="Modelo")
tree.heading("Pendência", text="Pendência")
tree.heading("Renavam", text="Renavam")
tree.heading("KM", text="KM")
tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Configurar o layout responsivo
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

list_veiculos()


# Iniciar o CustomTkinter
root.mainloop()