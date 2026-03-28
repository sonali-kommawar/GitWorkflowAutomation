from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    assigned_to = db.Column(db.String(50))
    status = db.Column(db.String(20))

    def __init__(self, title, assigned_to, status="Todo"):
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    developer = db.Column(db.String(50))
    status = db.Column(db.String(20))