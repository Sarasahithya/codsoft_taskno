class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("----- To-Do List -----")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
            print("----------------------")
    
    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f"Task {index} updated to '{new_task}'.")
        else:
            print("Invalid task index.")
    
    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print("Task {index} '{deleted_task}' deleted.")
        else:
            print("Invalid task index.")
    
    def menu(self):
        while True:
            print("\n----- To-Do List Menu -----")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                task = input("Enter task: ")
                self.add_task(task)
            
            elif choice == '2':
                self.view_tasks()
            
            elif choice == '3':
                index = int(input("Enter task index to update: "))
                new_task = input("Enter new task: ")
                self.update_task(index, new_task)
            
            elif choice == '4':
                index = int(input("Enter task index to delete: "))
                self.delete_task(index)
            
            elif choice == '5':
                print("Exiting To-Do List. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.menu()