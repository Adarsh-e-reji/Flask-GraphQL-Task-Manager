import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Execute a query to retrieve all tasks
cursor.execute('SELECT * FROM tasks')

# Fetch all rows from the executed query
tasks = cursor.fetchall()

# Print the retrieved data
for task in tasks:
    print(f"Task ID: {task[0]}, Name: {task[1]}")

# Close the connection
conn.close()
