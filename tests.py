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