'''
    script: Mahoney_M08_lab.py
    action: manages a to-do list using Task and ToDoList objects
    author: Erin Mahoney
    date:   07/20/2026
'''


class Task:
    # Represents one task in the to-do list.
    def __init__(self, description, priority):
        self.description = description
        self.status = "Incomplete"
        self.priority = priority

    def mark_complete(self):
        # Changes the task status to Complete.
        self.status = "Complete"

    def display_details(self):
        # Returns the task information as a formatted string.
        return (
            f"{self.description} - {self.status} - "
            f"Priority: {self.priority}"
        )


class ToDoList:
    # Stores and manages a list of Task objects.
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        # Creates a Task object and adds it to the list.
        new_task = Task(description, priority)
        self.tasks.append(new_task)
        print(
            f"Task '{description}' added with priority "
            f"'{priority}'."
        )

    def view_all_tasks(self):
        # Displays every task in the order it was added.
        print("\nYour To-Do List:")

        if not self.tasks:
            print("No tasks found.")
            return

        for task_number, task in enumerate(self.tasks, start=1):
            print(f"{task_number}. {task.display_details()}")

    def view_incomplete_tasks(self):
        # Displays only tasks with an Incomplete status.
        print("\nYour To-Do List:")
        incomplete_number = 1

        for task in self.tasks:
            if task.status == "Incomplete":
                print(
                    f"{incomplete_number}. "
                    f"{task.display_details()}"
                )
                incomplete_number += 1

        if incomplete_number == 1:
            print("No incomplete tasks found.")

    def complete_task(self):
        # Allows the user to mark one task as complete.
        self.view_all_tasks()

        if not self.tasks:
            return

        task_choice = input(
            "\nEnter the number of the task to mark as complete: "
        )

        if task_choice.isdigit():
            task_number = int(task_choice)

            if 1 <= task_number <= len(self.tasks):
                selected_task = self.tasks[task_number - 1]

                if selected_task.status == "Complete":
                    print(
                        f"Task '{selected_task.description}' "
                        "is already complete."
                    )
                else:
                    selected_task.mark_complete()
                    print(
                        f"Task '{selected_task.description}' "
                        "marked as complete."
                    )
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid task number.")


def display_menu():
    # Displays the program menu.
    print("\nMenu:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Incomplete Tasks")
    print("4. Complete Task")
    print("5. Quit")


def main():
    # Runs the interactive to-do list program.
    to_do_list = ToDoList()
    print("Welcome to the To-Do List!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input(
                "\nEnter a task description: "
            )

            priority = input(
                "Enter the task priority "
                "(High, Medium, Low): "
            ).capitalize()

            while priority not in ["High", "Medium", "Low"]:
                print("Please enter High, Medium, or Low.")
                priority = input(
                    "Enter the task priority "
                    "(High, Medium, Low): "
                ).capitalize()

            to_do_list.add_task(description, priority)

        elif choice == "2":
            to_do_list.view_all_tasks()

        elif choice == "3":
            to_do_list.view_incomplete_tasks()

        elif choice == "4":
            to_do_list.complete_task()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
