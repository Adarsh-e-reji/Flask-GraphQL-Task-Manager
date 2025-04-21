import sqlite3
import graphene

# Define Task type
class Task(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

# Define Query Class
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    tasks = graphene.List(Task)

    def resolve_hello(self, info, name):
        return f"Hello, {name}!"
    
    # Resolver to fetch all tasks from the database
    def resolve_tasks(self, info):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("SELECT id, name FROM tasks")
        rows = c.fetchall()
        conn.close()
        return [Task(id=row[0], name=row[1]) for row in rows]

# Define Mutation for creating tasks
class CreateTask(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    task = graphene.Field(Task)

    def mutate(self, info, name):
        
        # Insert new task into the SQLite database
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
        task_id = c.lastrowid
        conn.commit()
        conn.close()
        
        # Return the created task
        return CreateTask(task=Task(id=task_id, name=name))

# Define the Mutation class
class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()

# Define the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
