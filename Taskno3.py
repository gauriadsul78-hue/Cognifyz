import random
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
# Simple CRUD Task Manager

tasks = []

def create_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("✅ Task added successfully!")

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
                print("✏️ Task updated successfully!")
            else:
                print("❌ Invalid task number!")
        except:
            print("❌ Please enter a valid number!")

def delete_task():
    read_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Task '{removed}' deleted!")
            else:
                print("❌ Invalid task number!")
        except:
            print("❌ Please enter a valid number!")

# Main Menu
while True:
    print("\n==== TO-DO LIST MENU ====")
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
        print("❌ Invalid choice! Try again.")
