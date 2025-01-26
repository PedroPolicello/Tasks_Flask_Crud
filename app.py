from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
taskIdControl = 1

#CREATE
@app.route("/tasks", methods=["POST"])
def createTask():
    global taskIdControl
    data = request.get_json()
    newTask = Task(id=taskIdControl ,title=data["title"], description=data.get("description", ""))
    taskIdControl += 1
    tasks.append(newTask)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": newTask.id})


#READ
@app.route("/tasks", methods=["GET"])
def getTasks():
    taskList = [task.toDict() for task in tasks]

    output = {
        "tasks": taskList,
        "totalTasks": len(taskList)
    }
    return jsonify(output)


#READ
@app.route("/tasks/<int:id>", methods=["GET"])
def getTask(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.toDict())
        
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404


#UPDATE
@app.route("/tasks/<int:id>", methods=["PUT"])
def updateTask(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data ["title"]
    task.description = data ["description"]
    task.completed = data ["completed"]
    return jsonify({"message": "Tarefa atualizada com sucesso"})


#DELETE
@app.route("/tasks/<int:id>", methods=["DELETE"])
def deleteTask(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})


if(__name__ == "__main__"):
    app.run(debug=True)
