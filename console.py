#  To-Do List Console Application

todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main Program Loop is
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
