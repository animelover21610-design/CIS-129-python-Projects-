"""
script: Mahoney_M09_lab.py
action: Adds JSON file persistence to Gregory Sizer's Module 8 To-Do List.
original author: Gregory Sizer
modified by: Erin Mahoney
date: 28 July 2026
"""

from pathlib import Path
import json


class Task:
    # properties of a task
    description = ""
    priority = 0
    status = False

    # initialization when created
    def __init__(self, desc='', pri=1, sta=False):
        self.description = desc
        self.priority = pri
        self.status = sta


class ToDoList:
    """Store and manage Task objects."""

    def __init__(self):
        # Start with an empty list for this ToDoList object.
        self.toDoList = []

        # Keep tasks.json in the same folder as this Python file.
        # This makes the save location consistent every time the program runs.
        self.path = Path(__file__).resolve().parent / "tasks.json"

        # Load any tasks saved during a previous run.
        self.load_tasks()

    def load_tasks(self):
        """Load saved tasks from tasks.json when the program starts."""
        try:
            contents = self.path.read_text()
            task_list = json.loads(contents)

            # Rebuild Task objects from the saved dictionaries.
            for task_data in task_list:
                task = Task(
                    task_data["description"],
                    task_data["priority"],
                    task_data["status"]
                )
                self.toDoList.append(task)

            print(f"Loaded {len(self.toDoList)} saved task(s).")

        except FileNotFoundError:
            # The file will not exist the first time the program runs.
            # Continue normally with an empty list.
            print("No saved task file found. Starting with an empty list.")

        except json.JSONDecodeError:
            # If the file is empty or damaged, do not let the program crash.
            print("Saved task data could not be read. Starting with an empty list.")

    def save_tasks(self):
        """Save each task's description, priority, and status as JSON."""
        task_list = []

        # JSON cannot save Task objects directly, so convert each one
        # into a dictionary first.
        for task in self.toDoList:
            task_list.append({
                "description": task.description,
                "priority": task.priority,
                "status": task.status
            })

        contents = json.dumps(task_list, indent=4)
        self.path.write_text(contents)
        print(f"Saved {len(task_list)} task(s).")

    def add_task(self):
        """
        get a new task with priority from the user and append to the todo list
        add_task()
        """
        another = True
        while False != another:
            print("Add a task..")

            # get task description
            desc = input("Enter A Description [done to quit]: ")

            # check if user entered "done"
            if "done" == desc.lower():
                another = False
                break

            # get task priority
            priority = int(input("What Is The Priority [1-9 | 0 to quit]: "))

            # check if user entered a 0 priority
            if 0 == priority:
                another = False
                print(f"Discarding task with {priority} priority...")
                break

            # create task object instance with user provided parameters
            task_d = Task(desc, priority, False)

            # append the task to the todo list
            self.toDoList.append(task_d)

            # report what was done
            print(
                f"Added task: {task_d.description} with priority "
                f"{task_d.priority} as Incomplete."
            )

    def complete_task(self):
        """
        get selection information from the user to mark a task complete
        complete_task()
        """
        # list only the incomplete tasks
        self.list_tasks(False)

        # convert user input to an integer
        print("\n")
        selected = int(input("Which Task To Complete? "))

        # adjust selected task and report change
        self.toDoList[selected].status = True
        print(f"{self.toDoList[selected].description} marked COMPLETE.")

    def list_tasks(self, ALL_ITEMS=True):
        """
        list tasks from the todo list
        passing False in the ALL_ITEMS argument will return only incomplete items
        """
        print("\n")

        for item in self.toDoList:
            if ALL_ITEMS:
                # list all task items by default
                if item.status == False:
                    print(
                        f"{self.toDoList.index(item)}. {item.description} : "
                        f"Incomplete : Priority {item.priority}"
                    )
                else:
                    print(
                        f"{self.toDoList.index(item)}. {item.description} : "
                        f"Completed  : Priority {item.priority}"
                    )

            # list only INCOMPLETE items
            elif item.status == False:
                print(
                    f"{self.toDoList.index(item)}. {item.description} "
                    f"has Priority of {item.priority}"
                )


# main program
XIT = -1

greeting = "\n\tWelcome to Blanco Bronco To-Do List!\n"
farewell = "\n\tThank you for using Blanco Branco To-Do List!\n"

# the task manager
todo = ToDoList()


def menu():
    """Display the current menu for user selection."""
    print("\n")
    print(
        "\t1. List All Tasks "
        "\n\t2. List Incomplete Tasks "
        "\n\t3. Add A New Task "
        "\n\t4. Complete A Task "
        "\n\t0. Exit"
    )
    selected = int(input("\n\tEnter Selection: "))

    # List all tasks
    if 1 == selected:
        print("Schroedingers Tasks")
        todo.list_tasks(True)

    # List Incomplete tasks
    if 2 == selected:
        print("These tasks are INCOMPLETE.")
        todo.list_tasks(False)

    # Add a New Task
    if 3 == selected:
        print("Always more work to do:\n\n")
        todo.add_task()

    # Complete a Task
    if 4 == selected:
        print("Work Complete!")
        todo.complete_task()

    return selected


# The loop ends when the user selects 0.
# The finally block saves the task list whenever the program closes normally
# or is interrupted, helping prevent lost work.
try:
    while XIT != 0:
        print(greeting)
        XIT = menu()
finally:
    todo.save_tasks()
    print(farewell)
