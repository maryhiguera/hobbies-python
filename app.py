from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/hobbies.json")
def index():
    return db.hobbies_all()

@app.route("/hobbies.json", methods=["POST"])
def create():
    name = request.args.get("name")
    location = request.args.get("location")
    description = request.args.get("description")
    return db.hobbies_create(name, location, description)

@app.route("/hobbies/<id>.json")
def show(id):
    return db.hobbies_find_by_id(id)