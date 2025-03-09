import json
import os

class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f'Tarefa "{description}" adicionada com sucesso!')

    def list_tasks(self):
        if not self.tasks:
            print('Nenhuma tarefa encontrada.')
        else:
            for task in self.tasks:
                status = 'Concluída' if task['completed'] else 'Pendente'
                print(f"{task['id']}. {task['description']} [{status}]")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f'Tarefa {task_id} marcada como concluída!')
                return
        print(f'Tarefa {task_id} não encontrada.')

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f'Tarefa {task_id} removida com sucesso!')