from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# add app
app = Flask(__name__)
# add app config and db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# class model for functionality
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # a function that will return a string when we create a new element
    def __repr__(self):
        return '<Task %r>' % self.id


# give default route a place to live
# methods allow for data to POST and GET
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # create task content from text field in form
        task_content = request.form['content']
        # create a new object task
        new_task = Todo(content=task_content)

        # then try to save to db
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        # error handling
        except:
            return 'There was an issue adding your task, try again. This should\'nt really happen.'

    else:
        # return query of todos by date_created
        todos = Todo.query.order_by(Todo.date_created).all()
        # return the template page with list if todos to print out
        return render_template('index.html', todos=todos)


@app.route('/delete/<int:id>')
def delete_todo(id):
    task_to_delete = Todo.query.get_or_404(id)

    # try to delete todo
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    # error handling
    except:
        return 'There was an issue deleting your task, try again. This should\'nt really happen.'


# python defaults
if __name__ == '__main__':
    app.run(debug=True)
