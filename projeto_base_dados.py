# projeto de férias para fazer uma to-do lis

# declarando as tarefas em uma lista
# organizando cada tarefa em um dicionário diferente
import sqlite3

with sqlite3.connect("MINHA_LISTA_TAREFAS.db") as conn:
    cursor = conn.cursor()



def adicionar_tarefa(nometarefa,descricaoTarefa,prioridadetarefa):
    cursor.execute("INSERT INTO tarefas (nome, descricao,id,id_status) VALUES (?, ?,?,?)", 
                   (nometarefa, descricaoTarefa,prioridadetarefa,1))
    conn.commit()
    

def mostrar_tarefa():
    cursor.execute( "SELECT * FROM tarefas")
    rows = cursor.fetchone()
    while rows:
     print(rows)
     rows = cursor.fetchone()
    conn.commit()

def editar_tarefa(edit_status,num_tarefa):
    cursor.execute("UPDATE tarefas SET id_status = ? WHERE id_tarefas = ? ", (edit_status,num_tarefa))
    conn.commit()

def deletar_tarefas (tarefa_deletada):
    cursor.execute("DELETE FROM TAREFAS WHERE id_tarefas =?", (tarefa_deletada,))
    conn.commit()



print(10 * "--")
print("     To-do List")
print(10 * "--")

print("Menu:")
print("[1]  Adicionar Tarefa")
print("[2]  Mostrar Tarefas")
print("[3]  Marcar Tarefa como Concluída")
print("[4]  Remover Tarefas Concluídas")
print("[5]  Sair")

# While para rodar até o usuário pedir para sair e fazer break

while True:
    opcao = int(input("Digite a opção desejada: "))

    if opcao <= 0 or opcao > 5:
        print("Opção inválida.")

    if opcao == 1:
        nome_tarefa = input("Digite o nome da tarefa:")
        descricao = input("Digite a descrição da tarefa: ")
        prioridade = int(input("Qual a prioridade da tarefa? [1-alta, 2-media, 3-baixa]: "))

        adicionar_tarefa(nome_tarefa,descricao,prioridade)

    if opcao == 2:
        mostrar_tarefa()
    
    if opcao == 3:
        tarefa_a_editar = int(input("Digite o número da tarefa que deseja alterar o status"))
        editar_status = int(input("Digite qual status gostaria de trocar? \n1. Não iniciada \n2.Em prograsso\n3.Concluída"))
        
        editar_tarefa(editar_status,tarefa_a_editar)

    if opcao==4:
        deletar_opcao=int(input("Digite o número da tarefa que deseja deletar: "))
        
        deletar_tarefas(deletar_opcao)

    if opcao ==5:
        print("Saindo...")
        break


        

    
    

    