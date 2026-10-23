"""
Program: To-Do List v2 Functions
Purpose: Create a command-line to-do list program using functions, lists, tuples, loops, and conditionals.
Author: Erin Mahoney
Date: July 2026
"""

def show_menu():
    """Display the main menu options."""
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Incomplete Tasks")
    print("4. Complete Task")
    print("5. Quit")


def add_tasks(tasks):
    """Add tasks with a priority until the user types done."""
    print("\nAdd tasks to your list.")
    print("Type done when you are finished adding tasks.")

    task_name = input("Task Name: ")

    while task_name.lower() != "done":
        priority = input("Priority: ")

        # Each task is stored as a tuple: description, status, priority.
        task = (task_name, "Incomplete", priority)
        tasks.append(task)

        print("Task '" + task_name + "' added with priority '" + priority + "'.")

        task_name = input("\nTask Name: ")

    return tasks


def view_all_tasks(tasks):
    """Display all tasks in the list."""
    print("\nAll Tasks")

    if len(tasks) == 0:
        print("No tasks have been added.")
    else:
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i][0] + " - " + tasks[i][1] + " - Priority: " + tasks[i][2])


def view_incomplete_tasks(tasks):
    """Display only incomplete tasks."""
    print("\nIncomplete Tasks")

    if len(tasks) == 0:
        print("No tasks have been added.")
    else:
        incomplete_found = False

        for i in range(len(tasks)):
            if tasks[i][1] == "Incomplete":
                print(str(i + 1) + ". " + tasks[i][0] + " - " + tasks[i][1] + " - Priority: " + tasks[i][2])
                incomplete_found = True

        if incomplete_found == False:
            print("There are no incomplete tasks.")


def complete_task(tasks):
    """Mark a selected task as complete."""
    print("\nComplete a Task")

    if len(tasks) == 0:
        print("No tasks are available to complete.")
    else:
        view_all_tasks(tasks)

        task_number = int(input("Enter the task number to mark complete: "))

        if task_number >= 1 and task_number <= len(tasks):
            index = task_number - 1

            # Tuples cannot be edited directly, so this replaces the tuple
            # with a new tuple that has the status changed to Complete.
            completed_task = (tasks[index][0], "Complete", tasks[index][2])
            tasks[index] = completed_task

            print("Task Completed: " + tasks[index][0])
        else:
            print("Invalid task number.")

    return tasks


def main():
    """Control the main program loop."""
    tasks = []
    choice = ""

    while choice != "5":
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            tasks = add_tasks(tasks)
        elif choice == "2":
            view_all_tasks(tasks)
        elif choice == "3":
            view_incomplete_tasks(tasks)
        elif choice == "4":
            tasks = complete_task(tasks)
        elif choice == "5":
            print("Program Ends - Goodbye!")
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


main()
