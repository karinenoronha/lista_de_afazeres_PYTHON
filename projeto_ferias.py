# projeto de férias para fazer uma to-do lis

# declarando as tarefas em uma lista
# organizando cada tarefa em um dicionário diferente
tarefas = list()

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
        prioridade = input("Qual a prioridade da tarefa? [alta, media, baixa]: ")

        lista_tarefas = {
            "nome": nome_tarefa,
            "descrição": descricao,
            "prioridade": prioridade,
            "concluída": False  # Inicializando como não concluída
        }

        # Adicionando cada tarefa à lista de tarefas
        tarefas.append(lista_tarefas)
        print("Tarefa adicionada com sucesso!")

    elif opcao == 2:
        if not tarefas:
            print("Não existem tarefas adicionadas.")
            continue
        else:
            print("\n***** Tarefas pendentes *****")
            for i, lista_tarefas in enumerate(tarefas):
                if not lista_tarefas["concluída"]:
                    print(f"{i+1}. {lista_tarefas['descrição']} - Prioridade: {lista_tarefas['prioridade']}")

    elif opcao == 3:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluída"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido!")

    elif opcao == 4:
        tarefas = [lista_tarefas for lista_tarefas in tarefas if not lista_tarefas["concluída"]]
        print("Tarefas concluídas removidas com sucesso!")

    elif opcao == 5:
        print("Saindo do programa...")
        break

