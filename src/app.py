from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


#todos = []

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Agrega la nueva tarea a la lista de todos
    return jsonify(todos)  # Devuelve la lista de todos como un objeto JSON
   # return 'Response for the POST todo'


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):  # Comprueba si la posición está dentro del rango de la lista
        print("This is the position to delete: ", position)
        todos.pop(position)  # Elimina la tarea de la lista en la posición dada
    else:
        return 'Error: Position out of range', 400  # Retorna un error si la posición está fuera del rango
    return jsonify(todos)  # Retorna el jsonify de la lista de todos actualizada


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)