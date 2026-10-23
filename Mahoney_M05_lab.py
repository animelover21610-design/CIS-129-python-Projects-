"""
Script: Module 5 Part B Lab - To-Do List v1 Loops
Action: Creates an interactive to-do list that lets the user add, view, and complete tasks.
Author: Erin Mahoney
Date: 07/06/2026
"""

# Create an empty list to store tasks.
# Each task will be stored as a tuple: (description, status).
tasks = []

# This variable controls the main menu loop.
running = True

print("Welcome to the To-Do List!")

# The while loop keeps the program running until the user chooses to quit.
while running:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Option 1 allows the user to add tasks until they type done.
    if choice == "1":
        task = ""

        while task.lower() != "done":
            task = input("\nEnter a task (or type 'done' to finish): ")

            if task.lower() != "done":
                if task != "":
                    tasks.append((task, "Incomplete"))
                    print(f"Task '{task}' added.")
                else:
                    print("Task cannot be blank.")

    # Option 2 displays all tasks using a for loop.
    elif choice == "2":
        print("\nYour To-Do List:")

        if len(tasks) == 0:
            print("No tasks have been added yet.")
        else:
            for index in range(len(tasks)):
                description = tasks[index][0]
                status = tasks[index][1]
                print(f"{index + 1}. {description} - {status}")

    # Option 3 lets the user mark a task as complete.
    elif choice == "3":
        if len(tasks) == 0:
            print("\nThere are no tasks to complete.")
        else:
            print("\nYour To-Do List:")
            for index in range(len(tasks)):
                description = tasks[index][0]
                status = tasks[index][1]
                print(f"{index + 1}. {description} - {status}")

            task_number = input("Enter the number of the task to mark as complete: ")

            # isdigit() helps make sure the user entered a number before converting it.
            if task_number.isdigit():
                task_index = int(task_number) - 1

                if task_index >= 0 and task_index < len(tasks):
                    description = tasks[task_index][0]
                    tasks[task_index] = (description, "Complete")
                    print(f"Task '{description}' marked as complete.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    # Option 4 ends the program by changing running to False.
    elif choice == "4":
        running = False
        print("Goodbye!")

    # This handles menu choices that are not 1, 2, 3, or 4.
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
