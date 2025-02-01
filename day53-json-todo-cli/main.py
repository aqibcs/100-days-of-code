import json
import os


class TodoList:

    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)

        return []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"\n✅ Task '{task}' added.")

    def delete_task(self, task_index):
        """Delete a task from the list."""
        if 0 <= task_index < len(self.tasks):
            remove_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"\n❌ Task deleted'{remove_task['task']}")
        else:
            print("\n⚠️ Invalid task number.")

    def mark_completed(self, task_index):
        """Mark a task as completed by its index."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
            print(f"\n🎉 Task marked as completed: {self.tasks[task_index]['task']}")
        else:
            print("\n⚠️ Invalid task number. Please try again.")

    def display_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print("\n📭 Your to-do list is empty.")
        else:
            print("\n📋 Your to-do list:")
            for index, task in enumerate(self.tasks):
                status = "✅" if task['completed'] else "❌"
                print(f"{index + 1}. [{status}] {task['task']}")


def main():
    todo = TodoList()

    while True:
        print("\nWelcome to the To-Do List CLI 📝")
        print("1. ➕ Add a task")
        print("2. 📋 Display tasks")
        print("3. ❌ Delete a task")
        print("4. ✅ Mark a task as completed")
        print("5. 🚪 Exit")

        choice = input("\n👉 Enter your choice (1-5): ").strip()

        if choice == '1':
            task = input("\n📝 Enter the task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("\n⚠️ Task cannot be empty. Please try again.")
        elif choice == '2':
            todo.display_tasks()
        elif choice == '3':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_index = int(
                        input("\n🔢 Enter the task number to delete: "))
                    todo.delete_task(task_index)
                except ValueError:
                    print("\n⚠️ Invalid task number. Please try again.")
        elif choice == "4":
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_number = int(input("\n🔢 Enter the task number to mark as completed: "))
                    task_index = task_number - 1 
                    todo.mark_completed(task_index)
                except ValueError:
                    print("\n⚠️ Invalid input. Please enter a valid number.")
        elif choice == '5':
            confirm = input(
                "\n🤔 Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print("\n👋 Thank you for using the To-Do List CLI. Goodbye!")
                break
        else:
            print("\n⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
