from flask import Flask, render_template, request, session, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://Marco:Password1@ludus-parthenope-u9h85.mongodb.net/Homework?retryWrites=true&w=majority'
app.config['MONGO_DBNAME'] = 'Homework'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ricerca', methods=['POST'])
def ricerca():
    session.database = mongo.db
    return render_template('risultati.html')

if __name__ == '__main__':
    app.run()
app.secret_key = 'super secret key'
