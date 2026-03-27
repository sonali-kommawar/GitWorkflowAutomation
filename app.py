from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks as dictionary objects
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

# ADD TASK
@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task")
    member = request.form.get("member")

    if task_name:
        tasks.append({
            "name": task_name,
            "member": member,
            "status": "Todo"
        })

    return redirect(url_for("home"))

# UPDATE STATUS
@app.route("/update/<int:index>")
def update_status(index):
    if tasks[index]["status"] == "Todo":
        tasks[index]["status"] = "Doing"
    elif tasks[index]["status"] == "Doing":
        tasks[index]["status"] = "Done"

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)