from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Digite a descrição da tarefa: ")
            manager.add_task(description)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
            manager.complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Digite o ID da tarefa a ser removida: "))
            manager.remove_task(task_id)
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()