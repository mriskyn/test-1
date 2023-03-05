from flask import jsonify, request
from model import Todo
from helper import toJSON, datetimeNowFormatted
import uuid

todos = []

def apiGeneral() -> any:
  match request.method:
    case "POST":
      todo = request.get_json()
      now = datetimeNowFormatted()
      create_todo = Todo(str(uuid.uuid4()), todo['title'], todo['description'], None, now, now, None)
      todos.append(create_todo)
      return jsonify(toJSON(create_todo))
    case "GET":
      return jsonify(toJSON(todos))

def apiSpecify(id) -> any: 
  match request.method:
    case "GET":
      for item in todos:
        if (item.get_id() == id):
          return item.toJSON()

      return "No Data Retrieved"
    case "PUT" | 'PATCH':
      req_body = request.get_json()
      for item in todos:
        if (item.get_id() == id):
          item.set_update(req_body['title'], req_body['description'])
          return "Data Sucessfully Updated"

      return "No Action"
    case "DELETE":
      for item in todos:
        if (item.get_id() == id):
          item.set_delete()
          return "Data Successfully Deleted"

      return "No Action"
    case _:
      return "Methods not found"
    
def apiFinish(id) -> any: 
  if request.method == "PATCH":
    for item in todos:
      if (item.get_id() == id):
        item.set_finish()
        return "Data Successfully Updated"
    return "finished"