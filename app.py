from datetime import datetime

from flask import Flask, render_template
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
    return render_template('index.html')


# python defaults
if __name__ == '__main__':
    app.run(debug=True)
