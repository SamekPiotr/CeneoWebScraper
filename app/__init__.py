from flask import flask

app = Flask(__name__)

from ap import routes

if __name__ == '__main__':
    app.run(debug=True)