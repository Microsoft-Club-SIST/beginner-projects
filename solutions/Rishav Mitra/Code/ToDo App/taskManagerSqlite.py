import backend
import os
from tkinter import *

root = Tk()
root.geometry("620x450")
root.title("To Do App")

if not os.path.exists('tasksDatabase.db'):
	backend.createTable()

def add():
	task = newTaskEntry.get()
	backend.addNewTask(task)
	show()

def done():
	idc = doneEntry.get()
	backend.markTaskAsDone(idc)
	show()

def remove():
	backend.removeDoneTask()
	show()

def show():
	tasks.delete(1.0, END)
	rows = backend.showAllTasks()
	if len(rows) == 0:
		tasks.insert("end", "No tasks added")
	else:
		for row in rows:
			tasks.insert("end", f"{row[0]} | {row[1]} | {row[2]} \n\n")

	# tasksLabel.after(1000, show)

newTaskLabel = Label(root, text = "Add a new task")
newTaskLabel.grid(row = 0, column = 0, padx = 40)

newTaskEntry = Entry(root, font = "Arial")
newTaskEntry.grid(row = 1, column = 0, padx = 25, ipady = 5)

addTaskBtn = Button(root, text = "Add", command = add)
addTaskBtn.grid(row = 1, column = 1, ipadx = 5)

tasks = Text(root, height = 20, width = 40, font = "Arial")
tasks.grid(row = 2, column = 0, rowspan = 4, padx = 10, pady = 10)

doneLabel = Label(root, text = "Enter the id of any task you've completed")
doneLabel.grid(row = 2, column = 1)

doneEntry = Entry(root, font = "Arial")
doneEntry.grid(row = 3, column = 1)

okBtn = Button(root, text = "OK", command = done)
okBtn.grid(row = 4, column = 1)

removeBtn = Button(root, text = "Remove Done Tasks", command = remove)
removeBtn.grid(row = 5, column = 1)

show()
root.mainloop()
