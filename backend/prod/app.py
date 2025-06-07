from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Initialize MongoDB client
mongo = PyMongo(app)

@app.route('/')
def index():
    todos = mongo.db.todos.find().sort('created_at', -1)
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        todo = {
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.utcnow()
        }
        mongo.db.todos.insert_one(todo)
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    todo = mongo.db.todos.find_one({'_id': ObjectId(id)})
    if todo:
        mongo.db.todos.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'completed': not todo.get('completed', False)}}
        )
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    mongo.db.todos.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)
