# 📝 Simple To-Do List Manager – Pure Python

def show_menu():
    print("\n📝 To-Do List Manager")
    print("Choose an option:")
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Delete Task")
    print("[4] Exit")

def add_task(tasks):
    task = input("Enter the task to add: ")
    if task.strip():
        tasks.append(task)
        print("✅ Task added!")
    else:
        print("⚠️ Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks in your list.")
    else:
        print("📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"❌ Task '{removed}' deleted.")
            else:
                print("🚫 Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()