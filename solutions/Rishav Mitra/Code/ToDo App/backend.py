import sqlite3

def createTable():
	conn = sqlite3.connect('tasksDatabase.db')
	c = conn.cursor()

	c.execute("""CREATE TABLE tasks(
				id integer primary key autoincrement,
				name text,
				status text)""")

	conn.commit()
	conn.close()

def addNewTask(task):
	conn = sqlite3.connect('tasksDatabase.db')
	c = conn.cursor()

	c.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", (task, 'pending'))

	conn.commit()
	conn.close()

def markTaskAsDone(idc):
	conn = sqlite3.connect('tasksDatabase.db')
	c = conn.cursor()

	c.execute("UPDATE tasks SET status = 'done' WHERE id = (?)", (idc))

	conn.commit()
	conn.close()

def removeDoneTask():
	conn = sqlite3.connect('tasksDatabase.db')
	c = conn.cursor()

	c.execute("DELETE from tasks WHERE status = 'done'")

	conn.commit()
	conn.close()

def showAllTasks():
	conn = sqlite3.connect('tasksDatabase.db')
	c = conn.cursor()

	c.execute("SELECT * FROM tasks")

	rows = c.fetchall()
	return rows
