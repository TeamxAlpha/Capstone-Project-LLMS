from cli.commands import (
    add_task,
    list_tasks,
    mark_task_completed,
    remove_task,
)


def main() -> None:
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. List Pending Tasks")
        print("3. List Completed Tasks")
        print("4. Mark Completed Tasks")
        print("5. Remove a Task")
        print("6. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date: ")
            add_task(title, desc, due)
        elif choice == "2":
            list_tasks(False)
        elif choice == "3":
            list_tasks(True)
        elif choice == "4":
            try:
                task_id = int(input("Enter task Id to mark as completed: "))
                mark_task_completed(task_id)
            except ValueError:
                print("Enter a valid numeric task id")
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to remove: "))
                remove_task(task_id)
            except ValueError:
                print("Enter Valid numeric task ID: ")

        elif choice == "6":
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()

