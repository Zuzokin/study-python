from flask import Flask, request
import random

app = Flask(__name__)


# region Task 1
@app.get("/random-quote")
def get_random_quote():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()
        random_quotes = random.choice(quotes)
        return f"<h1>{random_quotes}</h1>"


# endregion


# region Task 2
@app.route("/api/convert-temperature", methods=["POST"])
def convert_temperature():
    data = request.json
    try:
        temp_to_convert = data["celsius"]
        fahrenheit_temp = temp_to_convert * 1.8 + 32
        return {"fahrenheit": fahrenheit_temp}, 200
    except KeyError:
        err = "Отсутствует значение 'celsius'"
        return {"error": err}, 400


# endregion


# region Task3
TASKS = {}


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    try:
        title = data["title"]
        description = data["description"]
    except KeyError:
        err = "Отсутствуют 'title' и/или 'description'"
        return {"error": err}, 400

    task_id = len(TASKS) + 1

    TASKS.update({task_id: {"title": title, "description": description}})
    return {
        "description": description,
        "task_id": task_id,
        "title": title,
    }


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = []
    for task_id, task in TASKS.items():
        task_list.append(
            {
                "description": task["description"],
                "title": task["title"],
                "task_id": task_id,
            }
        )
    return {"tasks": task_list}


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task():
    removed_task = TASKS.pop(id, None)
    if not removed_task(id):
        err = "Задача с указанным id не найдена"
        return {"error": err}, 400
    return {"message": "Задача успешно удалена"}


# endregion

if __name__ == "__main__":
    app.run(debug=True)
