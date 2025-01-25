from flask import Flask, request, jsonlify
from models.task import Task

app = Flask(__name__)

tasks = []
taskIdControl = 1

@app.route("/tasks", methods=["POST"])
def createTask():
    global taskIdControl
    data = request.get_json()
    newTask = Task(id=taskIdControl ,title=data["title"], description=data.get("description", ""))
    taskIdControl += 1
    tasks.append(newTask)
    return jsonlify({"message": "Nova tarefa criada com sucesso!"})


if(__name__ == "__main__"):
    app.run(debug=True)
