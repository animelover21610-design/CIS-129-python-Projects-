"""
Program: Module 7 To-Do List v3 Dictionaries
Purpose: Create a command-line to-do list using dictionaries, functions, lists, loops, and conditionals.
Author: Erin Mahoney
Date: July, 20 2026
"""


def show_menu():
    """Display the main menu options."""
    print("\nMenu:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Incomplete Tasks")
    print("4. Complete Task")
    print("5. Quit")


def add_tasks(tasks):
    """Add tasks with a priority until the user types done."""
    while True:
        task_name = input("Enter a task (or type 'done' to finish): ").strip()

        if task_name.lower() == "done":
            break

        if task_name == "":
            print("A task name cannot be blank.")
            continue

        priority = input("Enter the task priority (High, Medium, Low): ").strip().title()

        while priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Please enter High, Medium, or Low.")
            priority = input("Enter the task priority (High, Medium, Low): ").strip().title()

        # Each task is a dictionary with three descriptive keys.
        task = {
            "description": task_name,
            "status": "Incomplete",
            "priority": priority
        }
        tasks.append(task)

        print("Task '" + task_name + "' added with priority '" + priority + "'.")

    return tasks


def view_all_tasks(tasks):
    """Display all tasks in the list."""
    print("\nYour To-Do List:")

    if len(tasks) == 0:
        print("No tasks have been added.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(
                str(number) + ". "
                + task["description"] + " - "
                + task["status"] + " - Priority: "
                + task["priority"]
            )


def view_incomplete_tasks(tasks):
    """Display only tasks that are not complete."""
    print("\nIncomplete Tasks:")

    if len(tasks) == 0:
        print("No tasks have been added.")
    else:
        incomplete_found = False

        for number, task in enumerate(tasks, start=1):
            if task["status"] == "Incomplete":
                print(
                    str(number) + ". "
                    + task["description"] + " - "
                    + task["status"] + " - Priority: "
                    + task["priority"]
                )
                incomplete_found = True

        if incomplete_found == False:
            print("There are no incomplete tasks.")


def complete_task(tasks):
    """Mark a selected task as complete."""
    if len(tasks) == 0:
        print("\nNo tasks are available to complete.")
    else:
        view_all_tasks(tasks)
        task_number = input("\nEnter the number of the task to mark as complete: ").strip()

        if task_number.isdigit():
            index = int(task_number) - 1

            if index >= 0 and index < len(tasks):
                if tasks[index]["status"] == "Complete":
                    print("Task '" + tasks[index]["description"] + "' is already complete.")
                else:
                    # A dictionary is mutable, so its status value can be updated directly.
                    tasks[index]["status"] = "Complete"
                    print("Task '" + tasks[index]["description"] + "' marked as complete.")
            else:
                print("Invalid task number.")
        else:
            print("Invalid entry. Please enter a task number.")

    return tasks


def main():
    """Control the main program loop."""
    tasks = []
    choice = ""

    print("Welcome to the To-Do List!")

    while choice != "5":
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            tasks = add_tasks(tasks)
        elif choice == "2":
            view_all_tasks(tasks)
        elif choice == "3":
            view_incomplete_tasks(tasks)
        elif choice == "4":
            tasks = complete_task(tasks)
        elif choice == "5":
            print("\nGoodbye!")
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


main()
