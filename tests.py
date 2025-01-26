import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

def testCreateTask():
    newTaskData = {
        "title": "Nova tarefa",
        "descripiton": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json = newTaskData)
    assert response.status_code == 200
    responseJSON = response.json()
    assert "message" in responseJSON
    assert "id" in responseJSON
    tasks.append(responseJSON["id"])


def testGetTasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    responseJSON = response.json()
    assert "tasks" in responseJSON
    assert "totalTasks" in responseJSON


def testGetTask():
    if tasks:
        taskID = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{taskID}")
        assert response.status_code == 200
        responseJSON = response.json()
        assert taskID == responseJSON["id"]

def testUpdateTask():
    if tasks:
        taskID = tasks[0]
        payload = {
            "title": "Titulo atualizado",
            "description": "Nova descrição",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{taskID}", json=payload)
        assert response.status_code == 200
        responseJSON = response.json()
        assert "message" in responseJSON


        #Tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{taskID}")
        assert response.status_code == 200
        responseJSON = response.json()
        assert responseJSON["title"] ==  payload["title"]
        assert responseJSON["description"] ==  payload["description"]
        assert responseJSON["completed"] ==  payload["completed"]


def testDeleteTask():
    if tasks:
        taskID = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{taskID}")
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{taskID}")
        assert response.status_code == 404
