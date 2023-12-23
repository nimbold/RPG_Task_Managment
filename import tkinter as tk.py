from tkinter import Tk, Label, Entry, Button, Listbox

# Create the main window
window = Tk()
window.title("Task Manager RPG App")
window.geometry("400x300")

# Tasks list
tasks = []

# Function to add a task
def add_task():
    task_name = entry_task_name.get()
    task_description = entry_task_description.get()
    task = {"name": task_name, "description": task_description, "completed": False}
    tasks.append(task)
    update_task_list()

# Function to update the task list
def update_task_list():
    listbox_tasks.delete(0, "end")
    for task in tasks:
        task_status = "✓" if task["completed"] else " "
        listbox_tasks.insert("end", f"{task_status} {task['name']}")

# Task name label and entry
label_task_name = Label(window, text="Task Name:")
label_task_name.pack()
entry_task_name = Entry(window)
entry_task_name.pack()

# Task description label and entry
label_task_description = Label(window, text="Task Description:")
label_task_description.pack()
entry_task_description = Entry(window)
entry_task_description.pack()

# Add task button
button_add_task = Button(window, text="Add Task", command=add_task)
button_add_task.pack()

# Task list
listbox_tasks = Listbox(window)
listbox_tasks.pack()

# Start the main event loop
window.mainloop()