import tkinter as tk
from tkinter import messagebox

tasks = []


def update_count():
    count_label.config(text=f'Tasks: {len(tasks)}')


def add_task():
    task = task_entry.get().strip()
    if task == '':
        messagebox.showwarning('Warning', 'Enter a task')
        return

    tasks.append(task)
    listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    update_count()


def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning('Warning', 'Select a task')
        return

    index = selected[0]
    listbox.delete(index)
    tasks.pop(index)
    update_count()


def clear_tasks():
    if messagebox.askyesno('Confirm', 'Clear all tasks?'):
        listbox.delete(0, tk.END)
        tasks.clear()
        update_count()


root = tk.Tk()
root.title('📝 To-Do List')
root.geometry('600x450')
root.configure(bg='#f0f4f8')


title = tk.Label(root, text='📝 TO-DO LIST', font=('Arial', 22, 'bold'), bg='#f0f4f8', fg='#1f2937')
title.pack(pady=10)


task_entry = tk.Entry(root, width=35, font=('Arial', 13), bd=2)
task_entry.pack(pady=10)


count_label = tk.Label(root, text='Tasks: 0', font=('Arial', 11, 'bold'), bg='#f0f4f8', fg='#374151')
count_label.pack()


button_frame = tk.Frame(root, bg='#f0f4f8')
button_frame.pack(pady=8)

add_btn = tk.Button(button_frame, text='Add Task', command=add_task, font=('Arial', 11, 'bold'), width=15)
add_btn.pack(side='left', padx=5)


listbox = tk.Listbox(root, width=50, height=12, font=('Arial', 12), bd=2)
listbox.pack(pady=10)


delete_btn = tk.Button(button_frame, text='Delete Selected', command=delete_task, font=('Arial', 11, 'bold'), width=15)
delete_btn.pack(side='left', padx=5)

clear_btn = tk.Button(button_frame, text='Clear All', command=clear_tasks, font=('Arial', 11, 'bold'), width=15)
clear_btn.pack(side='left', padx=5)


update_count()

root.mainloop()