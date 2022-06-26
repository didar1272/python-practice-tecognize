from flask import Flask, redirect, render_template, request, url_for
import psycopg2
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    complete = db.Column(db.Boolean, nullable=True)
    body = db.Column(db.String(100), nullable=True)

    def __init__(self, title, complete):
        self.title = title
        self.complete = complete


@app.route('/')
@app.route('/<name>')
def home(name=None):
    todo_list = Todo.query.all()
    return render_template('todo.html', todo_list=todo_list)


@app.route('/add', methods=["POST"])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


# data = {}

# count = 0


# conn = psycopg2.connect(
#     host="localhost",
#     database="beflask",
#     user="postgres",
#     password="12345678a"
# )

# cur = conn.cursor()


# @app.route('/get-db')
# def get_db():
#     cur.execute('SELECT version()')

#     # display the postgreSQL db server version

#     db_version = cur.fetchone()
#     cur.close()
#     return 'True'


# class Todo:
#     def __init__(self, id, title):
#         self.id = id
#         self.title = title
#         self.complete = False


# @app.route('/new-todo', methods=["POST"])
# def new_todo():
#     title = request.form['title']
#     global count
#     count = count + 1
#     todo = Todo(count, title)
#     data[todo.id] = todo
#     return redirect(url_for('show_todo'))


# @app.route('/show-todo')
# def show_todo():
#     return render_template('todo.html', todo_list=data)


# @app.route('/update/<int:id>')
# def update(id):
#     todo = data[id]
#     todo.complete = True
#     return redirect(url_for('show_todo'))

    # @app.route('/<name>')
    # @app.route('/')
    # def index(name=None):
    #     print(name)
    #     return "Hello World!"

    # @app.route('/home')
    # def home():
    #     return "Hello to Home"


if __name__ == "__main__":
    app.run()
