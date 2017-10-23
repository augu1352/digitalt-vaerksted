import tkinter as tk
import random as rand
import csv
import os
import sys
from tkinter import messagebox

tasks = []


cwd = os.getcwd()

box_list = []

root = tk.Tk()
lb_tasks = tk.Listbox(root)
root.configure(bg="white")
root.title("Din Huskeseddel")
root.geometry("290x280")


def update_listbox():
    global tasks
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)


def sort_list_box():
    clear_listbox()
    for word in sorted(tasks):
        lb_tasks.insert("end", word)


def Save():
    global tasks
    with open("save.csv", "w") as f:
        writer = csv.writer(f, delimiter="\n")
        writer.writerow(tasks)


def Load():
    global tasks
    global lb_tasks
    with open("save.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            tasks.append(line)
        update_listbox()


def load_listbox():
    global tasks
    for task in tasks:
        lb_tasks.insert("end", task)
    update_listbox()


def clear_listbox():
    lb_tasks.delete(0, "end")


def add_task():
    global tasks
    task = txt_input.get()
    if task != "":
        if len(task) <= 30:
            tasks.append(task)
            txt_input.delete(0, "end")
            update_listbox()
        else:
            lbl_display["text"] = "A bit shorther next time"
            txt_input.delete(0, "end")
    else:
        messagebox.showwarning("WARNING", "You need to enter a task")
        txt_input.delete(0, "end")


def del_all():
    global tasks
    global lb_tasks
    if lb_tasks:
        confirmed = messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
        if confirmed:
            if os.path.isfile("save.csv"):
                os.remove("save.csv")
            tasks = []
        update_listbox()


def del_one():
    global tasks
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()


def sort_asc():
    global tasks
    update_listbox()
    tasks.sort()
    update_listbox()


def sort_desc():
    global tasks
    update_listbox()
    tasks.sort()
    tasks.reverse()
    update_listbox()


def chs_rand():
    task = rand.choice(tasks)
    lbl_display["text"] = task


def num_tasks():
    num_of_tasks = len(tasks)
    msg = "Number Of Tasks: %s" % (num_of_tasks)
    lbl_display["text"] = msg


def quit():
    if os.path.isfile("save.csv"):
        if os.stat("save.csv").st_size == 0:
            os.remove("save.csv")
    else:
        Save()
    sys.exit()


lbl_title = tk.Label(root, text="To-Do List", bg="white")
lbl_title.grid(row=0, column=0)

lbl_display = tk.Label(root, text="", bg="white")
lbl_display.grid(row=0, column=1)

txt_input = tk.Entry(root, width=25)
txt_input.grid(row=1, column=1)

btn_add_task = tk.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1, column=0)

btn_del_all = tk.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2, column=0)

btn_del_one = tk.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3, column=0)

btn_sort_asc = tk.Button(root, text="Sort (ABC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4, column=0)

btn_sort_desc = tk.Button(root, text="Sort (CBA)", fg="green", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5, column=0)

btn_chs_rand = tk.Button(root, text="Choose Random", fg="green", bg="white", command=chs_rand)
btn_chs_rand.grid(row=6, column=0)

btn_num_tasks = tk.Button(root, text="Number Of Tasks", fg="green", bg="white", command=num_tasks)
btn_num_tasks.grid(row=7, column=0)

btn_exit = tk.Button(root, text="Exit", fg="green", bg="white", command=quit)
btn_exit.grid(row=8, column=0)

lb_tasks.grid(row=2, column=1, rowspan=8)

if os.path.isfile("save.csv"):
    Load()


load_listbox()


root.mainloop()
