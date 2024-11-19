import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

with sqlite3.connect("MINHA_LISTA_TAREFAS.db") as conn:
    cursor = conn.cursor()

def adicionar_tarefa():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    prioridade = int(entry_prioridade.get())

    if nome == "":
        messagebox.showwarning("Aviso", "O nome da tarefa não pode estar vazio.")
        return
    
    if descricao == "":
        messagebox.showwarning("Aviso", "O nome da tarefa não pode estar vazio.")
        return
    

    cursor.execute("INSERT INTO tarefas (nome, descricao, id, id_status) VALUES (?, ?, ?, ?)",
                    (nome, descricao, prioridade, 1))    
    
    conn.commit()
    atualizar_lista_tarefas()
    limpar_campos()

def mostrar_tarefa():
    cursor.execute("SELECT * FROM tarefas")
    rows = cursor.fetchall()
    return rows

def editar_tarefa():
    tarefa_id = simpledialog.askinteger("Editar Tarefa",
                                        "Digite o número da tarefa que deseja editar: ")
    novo_status = simpledialog.askinteger("Editar Status", "Digite o status: 1. Não Iniciada | 2. Em Progresso | 3. Concluída")

    if tarefa_id and novo_status:
        cursor.execute("UPDATE tarefas SET id_status = ? WHERE id_tarefas=?", (novo_status, tarefa_id))
        conn.commit()
        atualizar_lista_tarefas()

def deletar_tarefas():
    tarefa_id = simpledialog.askinteger("Deletar Tarefas", "Digite o número da tarefa que deseja deletar")

    if tarefa_id:
        cursor.execute("DELETE FROM tarefas WHERE id_tarefas = ?", (tarefa_id,))
        conn.commit()
        atualizar_lista_tarefas()

def atualizar_lista_tarefas():
    listbox_tarefas.delete(0, tk.END)
    tarefas = mostrar_tarefa()

    for tarefa in tarefas:
        listbox_tarefas.insert(tk.END, f"ID:{tarefa[0]} | Nome: {tarefa[1]} | Prioridade: {tarefa[3]} | Status: {tarefa[4]}")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_prioridade.delete(0, tk.END)

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("500x400")

# Labels e caixas de entrada
label_nome = tk.Label(janela, text="NOME DA TAREFA: ")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_descricao = tk.Label(janela, text="DESCRIÇÃO DA TAREFA: ")
label_descricao.pack()
entry_descricao = tk.Entry(janela)
entry_descricao.pack()

label_prioridade = tk.Label(janela, text="PRIORIDADE [1. Alta | 2. Média | 3. Baixa]: ")
label_prioridade.pack()
entry_prioridade = tk.Entry(janela)
entry_prioridade.pack()

# Botão para adicionar tarefa
btn_adicionar_tarefa = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar_tarefa.pack()

# Lista de tarefas
label_tarefas = tk.Label(janela, text="LISTA DE TAREFAS: ")
label_tarefas.pack()

listbox_tarefas = tk.Listbox(janela, width=50, height=10)
listbox_tarefas.pack()

# Botões para editar e deletar tarefas
btn_editar_tarefas = tk.Button(janela, text="EDITAR TAREFAS", command=editar_tarefa)
btn_editar_tarefas.pack()

btn_deletar_tarefas = tk.Button(janela, text="DELETAR TAREFAS", command=deletar_tarefas)
btn_deletar_tarefas.pack()

# Atualizar a lista de tarefas quando a interface for aberta
atualizar_lista_tarefas()

# Rodar o loop principal da janela
janela.mainloop()


    
    
    
