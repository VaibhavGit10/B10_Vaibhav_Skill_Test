from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

DEV_DB_URI = os.getenv("DEV_DB_URI")
PROD_DB_URI = os.getenv("PROD_DB_URI")

dev_client = MongoClient(DEV_DB_URI)
prod_client = MongoClient(PROD_DB_URI)

dev_db = dev_client.get_database("dev")
prod_db = prod_client.get_database("prod")

dev_todos = dev_db.todos
prod_todos = prod_db.todos

@app.route("/")
def home():
    """Display welcome message on root route."""
    return render_template("welcome.html")

@app.route("/dev")
def dev():
    """Fetch dev database tickets and render them."""
    tasks = list(dev_todos.find({}, {"_id": 0, "title": 1, "description": 1, "completed": 1, "created_at": 1}))
    return render_template("index.html", tasks=tasks, env="Development")

@app.route("/prod")
def prod():
    """Fetch prod database tickets and render them."""
    tasks = list(prod_todos.find({}, {"_id": 0, "title": 1, "description": 1, "completed": 1, "created_at": 1}))
    return render_template("index.html", tasks=tasks, env="Production")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)