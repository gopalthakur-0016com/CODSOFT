from tkinter import *
from tkinter import messagebox

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()


def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")


def clear_tasks():
    if messagebox.askyesno("Clear All", "Do you want to delete all tasks?"):
        listbox.delete(0, END)
        save_tasks()


def save_tasks():
    tasks = listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file.readlines():
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass


# ---------------- GUI ---------------- #

root = Tk()

root.title("To Do List")
root.geometry("500x650")
root.configure(bg="white")
root.resizable(False, False)

heading = Label(
    root,
    text="TO DO LIST",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="blue"
)
heading.pack(pady=20)

task_entry = Entry(
    root,
    width=30,
    font=("Arial", 16)
)
task_entry.pack(pady=10)

task_entry.bind("<Return>", lambda event: add_task())

add_button = Button(
    root,
    text="Add Task",
    width=15,
    font=("Arial", 14),
    bg="blue",
    fg="white",
    command=add_task
)
add_button.pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    root,
    width=35,
    height=15,
    font=("Arial", 14),
    selectbackground="skyblue",
    yscrollcommand=scrollbar.set
)
listbox.pack(pady=20)

scrollbar.config(command=listbox.yview)

delete_button = Button(
    root,
    text="Delete Task",
    width=15,
    font=("Arial", 14),
    bg="red",
    fg="white",
    command=delete_task
)
delete_button.pack(pady=5)

clear_button = Button(
    root,
    text="Clear All",
    width=15,
    font=("Arial", 14),
    bg="orange",
    fg="white",
    command=clear_tasks
)
clear_button.pack(pady=5)

load_tasks()

root.mainloop()