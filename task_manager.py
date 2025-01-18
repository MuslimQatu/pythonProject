import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import json
from datetime import datetime
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = self.load_tasks()

        # Task input fields
        self.create_input_fields()

        # Task list
        self.create_task_list()

        # Buttons
        self.create_buttons()

    def create_input_fields(self):
        # Task name
        tk.Label(self.root, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
        self.task_name = tk.Entry(self.root, width=30)
        self.task_name.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        # Due date (Calendar)
        tk.Label(self.root, text="Due Date:").grid(row=1, column=0, padx=5, pady=5)
        self.calendar = Calendar(self.root, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Status
        tk.Label(self.root, text="Status:").grid(row=2, column=0, padx=5, pady=5)
        self.status = ttk.Combobox(self.root, values=["Not Started", "In Progress", "Completed"])
        self.status.set("Not Started")
        self.status.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Priority
        tk.Label(self.root, text="Priority:").grid(row=3, column=0, padx=5, pady=5)
        self.priority = ttk.Combobox(self.root, values=["Low", "Medium", "High"])
        self.priority.set("Medium")
        self.priority.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    def create_task_list(self):
        columns = ("name", "due_date", "status", "priority")
        self.task_list = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set up column headings with sorting enabled
        for col in columns:
            self.task_list.heading(
                col,
                text=col.replace("_", " ").title(),
                command=lambda _col=col: self.sort_tasks(_col, self.sort_directions[_col])
            )
            self.task_list.column(col, width=100)

        self.task_list.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        # Initialize sort directions (ascending for each column)
        self.sort_directions = {col: False for col in columns}

        self.update_task_list()


    def create_buttons(self):
        tk.Button(self.root, text="Add Task", command=self.add_task, bg="green").grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Modify Task", command=self.modify_task, bg="blue").grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="red").grid(row=4, column=2, padx=5, pady=5)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as file:
                    data = file.read().strip()
                    if not data:
                        return []
                    return json.loads(data)
            except json.JSONDecodeError:
                return []
        return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        name = self.task_name.get().strip()
        date = self.calendar.get_date()
        status = self.status.get()
        priority = self.priority.get()

        if not name:
            messagebox.showerror("Error", "Task name is required!")
            return

        task = {
            "name": name,
            "due_date": date,
            "status": status,
            "priority": priority
        }

        self.tasks.append(task)
        self.save_tasks()
        self.update_task_list()
        self.clear_fields()

    def modify_task(self):
        selected_item = self.task_list.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to modify!")
            return

        index = self.task_list.index(selected_item)
        name = self.task_name.get().strip()
        date = self.calendar.get_date()

        if not name:
            messagebox.showerror("Error", "Task name is required!")
            return

        self.tasks[index] = {
            "name": name,
            "due_date": date,
            "status": self.status.get(),
            "priority": self.priority.get()
        }

        self.save_tasks()
        self.update_task_list()
        self.clear_fields()

    def delete_task(self):
        selected_item = self.task_list.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return

        if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
            index = self.task_list.index(selected_item)
            del self.tasks[index]
            self.save_tasks()
            self.update_task_list()

    def sort_tasks(self, col, reverse=False):
        self.tasks.sort(key=lambda task: task[col], reverse=reverse)
        self.update_task_list()

        # Reverse the sort direction for the next click
        self.sort_directions[col] = not reverse

    def update_task_list(self):
        for item in self.task_list.get_children():
            self.task_list.delete(item)

        for task in self.tasks:
            self.task_list.insert("", "end", values=(
                task["name"],
                task["due_date"],
                task["status"],
                task["priority"]
            ))

    def clear_fields(self):
        self.task_name.delete(0, tk.END)
        self.calendar.selection_clear()
        self.status.set("Not Started")
        self.priority.set("Medium")
