# 📋 Building GraphQL APIs using Flask

A simple GraphQL API built using **Flask**, **Graphene**, and **SQLite** to manage a list of tasks. This project demonstrates how to build and interact with a GraphQL API using Python and serves as a great starter for anyone learning backend development or GraphQL.

---

## 📁 Project Structure
![Screenshot 2024-11-14 122903](https://github.com/Adarsh-e-reji/Flask-GraphQL-Task-Manager/blob/main/project2.png)


---

## 🚀 Features

-  **GraphQL Queries** – Fetch all tasks
-  **GraphQL Mutations** – Add a new task
-  **SQLite DB** – Lightweight database used for persistence
-  **Simple Structure** – Easy to read and extend

---

## 📦 Technologies Used

- **Python 3**
- **Flask**
- **Graphene (GraphQL for Python)**
- **Flask-GraphQL**
- **SQLite3**

---

## 🔧 Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```
```bash
# Activating virtual env - Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the project

```bash
python main.py
```
📍 The server will start at:
```bash
http://localhost:5001/graphql
```
Open this URL in your browser to use the GraphiQL interface and test queries or mutations.

---
## 🧪 Sample GraphQL Queries & Mutations

### Query:
-  **Default Greeting (Hello, World)**<br>

![Screenshot 2024-11-14 122903](https://github.com/Adarsh-e-reji/Flask-GraphQL-Task-Manager/blob/main/hello%20world.png)<br>
This screenshot shows the response when no name is passed to the hello query.


-  **Custom Greeting (Hello, Adarsh)**

![Screenshot 2024-11-14 122903](https://github.com/Adarsh-e-reji/Flask-GraphQL-Task-Manager/blob/main/name_adarsh.png)<br>
This screenshot shows the response when a name ("Adarsh") is passed to the hello query.

### Mutation:
-  **Create a New Task**<br>

![Screenshot 2024-11-14 122903](https://github.com/Adarsh-e-reji/Flask-GraphQL-Task-Manager/blob/main/sample%20task.png)<br>
This mutation creates a task named "Sample task 4".

---
## 📂 View Data Directly from the Database
If you want to view all tasks stored in the tasks.db directly to the console:
```bash
python view_data.py
```
![Screenshot 2024-11-14 122903](https://github.com/Adarsh-e-reji/Flask-GraphQL-Task-Manager/blob/main/db%20datas.png)<br>
This screenshot shows the data stored in the DataBase.

---
## 📚 Key Concepts

### Flask
**Flask** is a lightweight and flexible Python web framework used for building web applications. It's easy to get started with, making it ideal for both small and large-scale applications. Flask follows a minimalistic approach, allowing developers to choose the components they need, like database integration or form validation, making it highly customizable.

### GraphQL
**GraphQL** is a query language for APIs and a runtime environment for executing queries. Unlike REST, where the server defines the structure of responses, GraphQL allows clients to request exactly the data they need. This flexibility makes it efficient and reduces over-fetching of data. It uses a single endpoint for all queries and mutations.

### Mutation
In **GraphQL**, a **mutation** is a type of operation that allows you to modify data, such as creating, updating, or deleting items in the database. Mutations are similar to HTTP POST, PUT, or DELETE requests.

### Query
A **GraphQL query** is a read-only operation used to fetch data from the server. It is similar to the GET method in HTTP, allowing clients to specify what data they need, and the server responds accordingly.

### SQLite3
**SQLite** is a serverless, self-contained, and zero-configuration database engine. It is widely used for small to medium-sized applications, especially in mobile or embedded systems. **SQLite3** is the latest version of SQLite, providing a relational database with a simple file-based storage mechanism, making it ideal for projects like this one that require lightweight, local storage.


