from flask import Flask, render_template, request
import os

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    tasks.append(task)
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)