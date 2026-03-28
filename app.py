from flask import Flask, render_template, request, redirect, url_for
from database import db, Task

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB
with app.app_context():
    db.create_all()


# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    tasks = Task.query.all()
    return render_template("dashboard.html", tasks=tasks)


# ---------------- ADD TASK ----------------
@app.route("/add_task", methods=["POST"])
def add_task():
    title = request.form["title"]
    assigned = request.form["assigned"]

    new_task = Task(title, assigned)

    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("dashboard"))


# ---------------- UPDATE STATUS ----------------
@app.route("/update/<int:id>")
def update(id):
    task = Task.query.get(id)

    if task.status == "Todo":
        task.status = "Doing"
    elif task.status == "Doing":
        task.status = "Done"

    db.session.commit()
    return redirect(url_for("dashboard"))


# ---------------- DELETE TASK ----------------
@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)