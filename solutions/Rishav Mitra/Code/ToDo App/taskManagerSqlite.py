import backend
import os

if not os.path.exists('tasksDatabase.db'):
	backend.createTable()

while True:
	print("\nWhat would you like to do ?")
	print("***************************")

	print("1. Show all tasks")
	print("2. Add a new task")
	print("3. Mark a task as done")
	print("4. Remove all tasks which are done")
	print("5. Quit app")
	response = input()

	if response == '1':
		print("id |  task  | status ")
		print("---------------------")
		rows = backend.showAllTasks()
		if len(rows) == 0:
			print("No tasks added")
		else:
			for row in rows:
				print(f"{row[0]} | {row[1]} | {row[2]} ")
	elif response == '2':
		task = input("Enter task ")
		backend.addNewTask(task)
	elif response == '3':
		idc = input("Enter id of the task you have completed ")
		backend.markTaskAsDone(idc)
	elif response == '4':
		backend.removeDoneTask()
	elif response == '5':
		break
	else:
		print("Invalid option")
