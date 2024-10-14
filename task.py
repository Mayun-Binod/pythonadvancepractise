import os

# Load tasks from a file (if exists)
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    else:
        tasks = []
    return tasks

# Save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTodo List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Mark a task as completed
def complete_task(tasks):
    task_num = int(input("Enter the task number to complete: "))
    if 0 < task_num <= len(tasks):
        completed_task = tasks.pop(task_num - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task number.")

# Main function
def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
