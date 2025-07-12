import tkinter as tk
from tkinter import messagebox
import json
import os
import sys

TODO_FILE = "todo.json"

# Get the absolute path to the icon (compatible with PyInstaller)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks():
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f)

# Add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Initialize window
root = tk.Tk()
root.title("BossM TODO App")
root.geometry("400x400")

# Load .ico icon safely
icon_path = resource_path("bossm.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

tasks = load_tasks()

# UI Components
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_btn.pack()

# Load tasks into listbox
for task in tasks:
    listbox.insert(tk.END, task)

# Start the app
root.mainloop()
