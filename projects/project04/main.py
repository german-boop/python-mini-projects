tasks = []

while True:
    print("\n1. Add task\n2. Show tasks\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        print("\nYour tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
