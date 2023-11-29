from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append({"task": task, "status": "Pending"})
    enumerated_tasks = [(idx + 1, task) for idx, task in enumerate(tasks)]
    return render_template("index.html", tasks=enumerated_tasks)

@app.route("/mark_complete/<int:task_id>", methods=["GET"])
def mark_complete(task_id):
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["status"] = "Completed"
    return redirect(url_for("index"))

@app.route("/remove_task/<int:task_id>", methods=["GET"])
def remove_task(task_id):
    if 1 <= task_id <= len(tasks):
        del tasks[task_id - 1]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
def mark_complete(task_id):
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["status"] = "Completed"
    return redirect("/")

@app.route("/remove_task/<int:task_id>", methods=["GET"])
def remove_task(task_id):
    if 1 <= task_id <= len(tasks):
        del tasks[task_id - 1]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)