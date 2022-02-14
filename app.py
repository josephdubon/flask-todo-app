# import flask
from flask import Flask, render_template

# add app
app = Flask(__name__)


# give default route a place to live
@app.route('/')
def index():
    return render_template('index.html')


# python defaults
if __name__ == '__main__':
    app.run(debug=True)
