from itertools import count
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


data = {}

count = 0


class Todo:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.complete = False


@app.route('/new-todo', methods=["POST"])
def new_todo():
    title = request.form['title']
    global count
    count = count + 1
    todo = Todo(count, title)
    data[todo.id] = todo
    return redirect(url_for('show_todo'))


@app.route('/show-todo')
def show_todo():
    return render_template('todo.html', todo_list=data)


@app.route('/update/<int:id>')
def update(id):
    todo = data[id]
    todo.complete = True
    return redirect(url_for('show_todo'))

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
