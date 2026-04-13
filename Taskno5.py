import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

def create_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added & saved!")

def read_tasks():
    if not tasks:
        print("📭 No tasks available.")
    else:
        print("\n📋 Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    read_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[num - 1] = new_task
                save_tasks(tasks)
                print("✏️ Task updated & saved!")
            else:
                print("❌ Invalid number!")
        except:
            print("❌ Enter valid input!")

def delete_task():
    read_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑️ '{removed}' deleted & saved!")
            else:
                print("❌ Invalid number!")
        except:
            print("❌ Enter valid input!")

# Menu
while True:
    print("\n==== TASK MANAGER (FILE STORAGE) ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_task()
    elif choice == '2':
        read_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice!")
