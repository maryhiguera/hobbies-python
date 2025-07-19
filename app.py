from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/hobbies.json")
def index():
    return db.hobbies_all()